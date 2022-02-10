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
$python -m build
``` 
Then you will see a new folder named `dist/` which contains the `.tar.gz` and `.whl` file for
distribution.

# Deploy in Heroku

For deploy in Heroku you need first login to your account and then run the following commands:

- Run container login
```bash
$heroku container:login
```
Then create a new app, choose a name for your app, for example I will use `your-app-name`

```bash
$heroku create your-app-name
```
Now you need to push your container and link it to your app
```bash
$heroku container:push web -a your-app-name
```
Last step is release 
```bash
$heroku container:release web -a your-app-name
```
Now you can access your app at `your-app-name.herokuapp.com/docs`


