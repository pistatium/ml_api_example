FROM python:3.7-slim
WORKDIR /opt/api
RUN apt-get update && apt-get -y install build-essential && pip install pipenv
COPY Pipfile /opt/api
COPY Pipfile.lock /opt/api
RUN pipenv install
COPY src/ /opt/api
ENV PYTHONPATH=/opt/api/src
