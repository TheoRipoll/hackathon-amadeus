# django_hackathon_amadeus

## Prerequisites

- Python 3.6 or higher
- Node.js 10.16 or higher

## Step 1 - Create a virtual environment

install virtualenv:

    python -m pip install --user virtualenv

create a virtual environment:

    python -m venv .venv

activate virtualenv:

    .venv\Scripts\Activate.ps1

## Step 2 - Install requirements

    pip install -r requirements.txt

## step 3 - static files

    python manage.py collectstatic 

## step 4 - create superuser

    python manage.py createsuperuser

## step 5 - bdd

    python manage.py migrations

    python manage.py migrate

## step 4 - Run Server

    cd backend

    python manage.py runserver

    http://127.0.0.1:8000/

