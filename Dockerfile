FROM python:3.8-alpine

RUN mkdir /data
COPY . /data/
WORKDIR /data

RUN pip install git+https://github.com/fair-software/badge

ENTRYPOINT ["howfairis"]
