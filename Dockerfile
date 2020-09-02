FROM python:3.8-alpine

RUN mkdir /data
COPY . /data/
WORKDIR /data

CMD ["/bin/sh", "/data/check.sh"]
