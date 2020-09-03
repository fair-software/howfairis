# badge
A badge for showing compliance with fair-software.eu



Building the docker image:

```shell
# (from project root directory)
docker build -t howfairis .
```

Running the dockerized howfair is locally:

```shell
# (from project root directory)
docker run -ti howfairis
```

Non-dockerized howfairis:

```shell
# Create a virtualenv, e.g. with
python3 -m virtualenv venv3

# activate virtualenv
source venv3/bin/activate

# (from the project root directory)
# install howfairis as an editable package
pip install --editable .
```

