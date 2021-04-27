FROM python:3.9-slim-buster

# copy the dependencies file to the working directory
COPY requirements.txt .
# install dependencies
RUN apt-get update -y
RUN pip install -r requirements.txt
RUN apt-get install libglib2.0-0 -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install --reinstall libxcb-xinerama0 -y
COPY . .

CMD [ "python", "emotQT.py" ]