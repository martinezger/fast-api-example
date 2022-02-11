# A Fast Api example Project
This application expose an api rest for handling User and User's tasks.
This example contains docker conotainer to run locally and steps to deploy in heroku.

# Run Local Test Server
This application use docker and docker compose to run a local server. So first make sure you
have this two installed in your pc.

Steps to run the local server:

```bash
$ docker-compose up
```
After application start you can access the OpenApi documentation at [http:://localhost:5002/docs](http://localhost:5002/docs)

# Run Local Development Server

You need to create a virtualenv and install the dependencies with pip:
```bash
$ python3 -m venv $PWD/myvenv
$ source myvenv/bin/activate
$ pip install -r requirements.txt
```

For test your development you can run the application in debug mode like this:

```bash
$ python src/setups/runapp.py --debug
```
 After application start you can access the OpenApi documentation in [http:://localhost:5002/docs](http://localhost:5002/docs)
 
 # Run tests
 In order to run the unit test suit, first you need to setup the PYTHONPATH envvar like this
 
```bash
$ export PYTHONPATH=$PWD/src
```
For run test do
```bash
$ python -m pytest test
```
# Build for Distribution
If you need build a distribution package run the following command:
```bash
$ python -m build
``` 
Then you will see a new folder named `dist/` which contains the `.tar.gz` and `.whl` file for
distribution.

# Deploy in Heroku

For deploy in Heroku you need first login to your account and then run the following commands:

- Run container login
```bash
$ heroku container:login
```
Then create a new app, choose a name for your app, for example I will use `your-app-name`

```bash
$ heroku create your-app-name
```
Now you need to push your container and link it to your app
```bash
$ heroku container:push web -a your-app-name
```
Last step is release 
```bash
$ heroku container:release web -a your-app-name
```
Now you can access your app at `your-app-name.herokuapp.com/docs`


# Deploy in Kubernetes

This project has two yml files, `deployment.yml` and `service.yml` both are for deploy in kubernets with
the following commands. 
If you want to run this local you need to install first minikube.

```bash
$ kubectl create -f deployment.yml
$ kubectl create -f service.yml
``` 
In order to get service port.
```bash
$ kubectl get svc
```
The command will diplay something like the follow output

```bash
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)          AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP          4m47s
python-api   NodePort    10.99.4.56   <none>        5002:32180/TCP   80s
```

the port assigned to our service is 32180. Then you need to get your minikube ip address, run this

```bash
$ kubectl cluster-info

Kubernetes master is running at https://192.168.99.103:8443
KubeDNS is running at https://192.168.99.103:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy
```

the server ip is the kubernetes master one. Now you can go to your browser and type 192.168.99.103:32180/docs.

You need to have in count k8s will assing random port to the service so the before ip and port will vary for you.
 
