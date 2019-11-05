FROM python:3.6.8-alpine

LABEL image for a very simple flask application

WORKDIR /

COPY . .

RUN ["pip3", "install","-r", "requirements.txt"]

CMD  python flask-auth.py