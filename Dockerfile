FROM python:3.10-slim-bullseye

WORKDIR /app

RUN apt-get update
RUN pip install --upgrade pip

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

RUN apt-get update

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

COPY . /app


CMD gunicorn --bind 0.0.0.0:$PORT --chdir src --workers 1 --threads 8 --timeout 0 shopify_crm.shopify_crm.wsgi
