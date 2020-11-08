# Teacheress Backend

Here we deploy a python fast api backend that serves and stores appointments.

- `controller`is a package with all the controller defining different endpoints
- `models` Basic model definitions go here.

## Requirements

- python3.8, pip

    >>> pip install -r requirements.txt

See `requierements.txt` for a list of all packages.


## First steps

Create a virtual environment and activate it.

    >>> python -m venv .venv
    >>> .venv/Activate.ps1

Install the requirements and run the setup.

    (.venv) >>> pip install -r requirements.txt
    (.venv) >>> python setup.py develop

Test the app using pytest

    >>> pytest

And run the service

    >>> uvicorn teacheress.main:app

Go see the local docs on http://localhost:8000/docs
