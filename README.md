## Set up

Either build and use the supplied docker image:

1. `docker build -t sampeka/rover .`
2. `docker run -ti sampeka/rover`

Or set up a virtual environment and install dependencies:

1. Set up a virtualenv with python 3.8.2
2. `pip install -r requirements.txt`
3. `python -m rover`

## Commands

- Run the cli: `python -m rover`
- Run the test suite: `py.test -vv`
- Run the static type checker: `mypy ./rover`
