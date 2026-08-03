# Productivity API

A Flask REST API for managing users and personal notes using JWT authentication.

## Features

- User registration
- User login
- JWT authentication
- Create notes
- View notes
- Update notes
- Delete notes
- Password hashing with Flask-Bcrypt
- Database migrations with Flask-Migrate

## Technologies

- Python 3.12
- Flask
- Flask-RESTful
- Flask-JWT-Extended
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- SQLite

## Installation

Clone the repository:

```bash
git clone https://github.com/kipkoechbrian-dot/flask-c10-summative-lab-sessions-and-jwt-clients.git
```

Move into the backend folder:

```bash
cd backend
```

Install dependencies:

```bash
pipenv install --skip-lock
```

Activate the virtual environment:

```bash
pipenv shell
```

## Database

Initialize migrations:

```bash
flask db init
```

Create migration:

```bash
flask db migrate -m "Initial migration"
```

Apply migration:

```bash
flask db upgrade
```

Seed the database:

```bash
python seed.py
```

## Running the Server

```bash
flask --app app run
```

Server runs at:

```
http://127.0.0.1:5000
```

## API Endpoints

### Authentication

POST /signup

POST /login

GET /me

### Notes

GET /notes

POST /notes

PATCH /notes/<id>

DELETE /notes/<id>

## Author

Brian Kipkoech