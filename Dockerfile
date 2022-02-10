FROM python:3.9-buster
WORKDIR /usr/src
COPY . .
RUN pip install --upgrade pip
RUN pip install -q build
RUN python3 -m build
RUN pip install dist/api_rest-0.0.1-py3-none-any.whl
CMD ["runapp"]
