FROM python:alpine3.9
COPY . /app
WORKDIR /app
RUN pip install .
ENTRYPOINT ["howfairis"]
