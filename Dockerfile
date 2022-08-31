FROM python:3.10.6-alpine3.16
COPY . /app
WORKDIR /app
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install .
ENTRYPOINT ["howfairis"]
