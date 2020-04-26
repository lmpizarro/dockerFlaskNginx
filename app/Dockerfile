FROM python:3.7-slim
 
RUN apt-get update
RUN apt-get upgrade -y

RUN apt-get install openntpd -y


RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY  . .

