FROM python:3.9

WORKDIR /app

COPY ./bolt_app/requirements.txt /app

RUN pip3 install -r requirements.txt
