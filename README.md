# circleci-codecov-demo

[![GitHub](https://img.shields.io/github/license/marwanali1/circleci-codecov-demo?color=g)](https://github.com/marwanali1/circleci-codecov-demo/blob/develop/LICENSE)
[![CircleCI](https://img.shields.io/circleci/build/github/marwanali1/circleci-codecov-demo/develop)](https://circleci.com/gh/marwanali1/circleci-codecov-demo/tree/develop)
[![Codecov](https://img.shields.io/codecov/c/github/marwanali1/circleci-codecov-demo)](https://codecov.io/gh/marwanali1/circleci-codecov-demo)

Repo for learning how to integrate CircleCI and Codecov with python codebase

### Usage:
Clone the repo: `git clone https://github.com/marwanali1/circleci-codecov-demo.git`

Change into it: `cd circleci-codecov-demo`

Export python path: `export PYTHONPATH=$PWD`  

Install dependencies: `pipenv install`

Start virtual env: `pipenv shell`

Run tests `python3 tests/test_math_functions.py`

Run tests with coverage: `pipenv run coverage run tests/test_math_functions.py`

Leave virtual env: `exit`