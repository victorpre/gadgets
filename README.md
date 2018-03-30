# Simple django REST API using Django Rest Framework

[![Build Status](https://travis-ci.org/victorpre/gadgets.svg?branch=master)](https://travis-ci.org/victorpre/gadgets)


## Running:

Backend:

- `make build-backend`
- `make run-backend`

Frontend:

- `make run-frontend`

## Development Instructions:

- `git clone https://github.com/victorpre/gadgets.git && cd gadgets`
- `virtualenv -p python3 venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python backend/manage.py migrate`
- `python backend/manage.py runserver`


## Testing

- `python backend/manage.py test`
