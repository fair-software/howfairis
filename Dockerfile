FROM python:3.8-alpine

RUN apk add git

WORKDIR /data

RUN pip install git+https://github.com/fair-software/badge@url

ENTRYPOINT ["howfairis"]
