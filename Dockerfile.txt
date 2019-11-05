FROM python:3.6.8-alpine

LABEL image for a very simple flask application

WORKDIR /

COPY . .

RUN ["pip3", "install", "pipenv"]

RUN ["pipenv", "install"]

CMD pipenv run python flask-auth.py