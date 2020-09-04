FROM python:3.8-alpine

RUN apk add git

RUN mkdir /data
COPY . /data/
WORKDIR /data

RUN pip install git+https://github.com/fair-software/badge@url

ENTRYPOINT ["howfairis"]
