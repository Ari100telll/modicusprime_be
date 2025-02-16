FROM python:3.11.8-slim
RUN apt-get update -y
WORKDIR /usr/src/app
COPY /requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . .
