FROM python:3.13.2-alpine3.21

COPY . /app
# see also .dockerignore

WORKDIR /app

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install .

ENTRYPOINT ["howfairis"]
