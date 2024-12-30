# Theatre API

## Introduction
This project is an RESTful API service for manage theatre written on Django.

## Features
* Authentication with JWT
* Authorization with permissions
* Admin panel via /admin/
* Image upload via /upload-image/
* Swagger documentation via /api/doc/swagger/
* Managing reservations and tickets
* Creating plays with genres and actors
* Creating plays, theatre halls
* Creating performances
* Managing props for individual performances
* Filtering performances by date and play
* Filtering plays by title, genre and actor
* Pagination reservations

## Installing with GitHub
Install PostgreSQL and create a database.
There is .env.sample file to see how to set environment variables.

  ```bash
  git clone the-link-from-your-forked-repo
  cd theatre-api
  git checkout -b <name of your branch>
  python -m venv venv
  venv\Scripts\activate (on Windows)
  source venv/bin/activate (on macOS)
  pip install -r requirements.txt
  set DJANGO_SECRET_KEY=<your secret key>
  set POSTGRES_DB=<your db name>
  set POSTGRES_USER=<your db username>
  set POSTGRES_HOST=<your db hostname>
  set POSTGRES_PORT=<your postgres port>
  set POSTGRES_PASSWORD=<your postgres password>
  python manage.py migrate
  python manage.py runserver
  ```

### Run with Docker
  ```bash
  docker compose build
  docker compose up
  ```

## Getting access
  * Get access token via ```/api/user/token/```
  * Enter Test User credentials

## Test User
* Email: admin@admin.com
* Password: admin
