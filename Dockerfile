FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN \
  apt-get -y update && \
  apt-get install -y gettext && \
  apt-get clean

ADD . /opt/marketplace
WORKDIR /opt/marketplace/django_app

RUN pip install pipenv && pipenv install --system --deploy --three

EXPOSE 8000
ENV PORT 8000
