FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN pip install flask celery redis flask-sqlalchemy flask-wtf
WORKDIR /app

