# set base image (host OS)
FROM python:3.9-slim-buster

# copy the dependencies file to the working directory
COPY src/requirements.txt .
# install dependencies
RUN pip install -r requirements.txt
