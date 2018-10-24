FROM python:3.6-slim
WORKDIR /opt/api
RUN apt-get update -y && apt-get -y install build-essential && pip install pipenv
COPY Pipfile /opt/api
COPY Pipfile.lock /opt/api
RUN pipenv install
COPY src/ /opt/api
ENV PYTHONPATH=/opt/api/src
ENV APP_HOST=0.0.0.0
ENV APP_PORT=8000

CMD pipenv run python main.py
