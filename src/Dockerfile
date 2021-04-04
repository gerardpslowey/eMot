# set base image (host OS)
FROM python:3.9-slim-buster
# copy the dependencies file to the working directory
COPY requirements.txt .
# install dependencies
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm
RUN python -m nltk.downloader punkt
