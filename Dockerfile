FROM python:3.6-slim

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY  ./requirements.txt /code/requirements.txt

RUN pip install -r /code/requirements.txt

COPY . /code/

WORKDIR /code/
