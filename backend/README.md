# Productivity API - Flask JWT Authentication and Notes Management

A secure RESTful API built with Flask that allows users to register, log in using JSON Web Tokens (JWT), and manage personal notes. Each user can only access, update, and delete their own notes.

---

## Features

- User Registration
- User Login
- Password Hashing using Flask-Bcrypt
- JWT Authentication
- Protected Routes
- Create Notes
- View Notes
- Update Notes
- Delete Notes
- SQLite Database
- Flask-Migrate Database Migrations
- Marshmallow Serialization

---

## Technologies Used

- Python 3.12
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- Flask-Bcrypt
- Marshmallow
- SQLite
- Pipenv

---

## Project Structure

backend/

├── app.py

├── config.py

├── models.py

├── schemas.py

├── seed.py

├── Pipfile

├── resources/

│ ├── auth.py

│ └── notes.py

├── migrations/

├── instance/

└── README.md

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/kipkoechbrian-dot/flask-c10-summative-lab-sessions-and-jwt-clients.git
```

---

### 2. Navigate into the project

```bash
cd flask-c10-summative-lab-sessions-and-jwt-clients/backend
```

---

### 3. Install Pipenv

```bash
pip install pipenv
```

---

### 4. Install dependencies

```bash
pipenv install
```

If Pipfile.lock causes dependency issues:

```bash
pipenv install --skip-lock
```

---

### 5. Activate the virtual environment

```bash
pipenv shell
```

---

### 6. Initialize the database

```bash
flask db init
```

---

### 7. Generate migrations

```bash
flask db migrate -m "Initial migration"
```

---

### 8. Apply migrations

```bash
flask db upgrade
```

---

### 9. Seed the database

```bash
python seed.py
```

Expected output

```
Deleting existing data...
Creating users...
Creating notes...
Database seeded successfully!
```

---

### 10. Start the server

```bash
flask --app app run
```

Server

```
Running on http://127.0.0.1:5000
```

---

## Database Verification

Check that the tables were created.

```bash
sqlite3 instance/app.db ".tables"
```

Expected Output

```
alembic_version
users
notes
```

---

## API Endpoints

### Register

POST

```
/signup
```

Example

```bash
curl -X POST http://127.0.0.1:5000/signup \
-H "Content-Type: application/json" \
-d '{"username":"brian","password":"1234"}'
```

---

### Login

POST

```
/login
```

```bash
curl -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"username":"brian","password":"1234"}'
```

Returns

- User information
- JWT Access Token

---

### Current User

GET

```
/me
```

```bash
curl http://127.0.0.1:5000/me \
-H "Authorization: Bearer YOUR_TOKEN"
```

---

### Create Note

POST

```
/notes
```

```bash
curl -X POST http://127.0.0.1:5000/notes \
-H "Authorization: Bearer YOUR_TOKEN" \
-H "Content-Type: application/json" \
-d '{"title":"Shopping","content":"Buy milk"}'
```

---

### View Notes

GET

```
/notes
```

```bash
curl http://127.0.0.1:5000/notes \
-H "Authorization: Bearer YOUR_TOKEN"
```

---

### Update Note

PATCH

```
/notes/1
```

```bash
curl -X PATCH http://127.0.0.1:5000/notes/1 \
-H "Authorization: Bearer YOUR_TOKEN" \
-H "Content-Type: application/json" \
-d '{"title":"Updated Title"}'
```

---

### Delete Note

DELETE

```
/notes/1
```

```bash
curl -X DELETE http://127.0.0.1:5000/notes/1 \
-H "Authorization: Bearer YOUR_TOKEN"
```

---

## Routes

View all available routes

```bash
flask --app app routes
```

Expected Output

```
/
/signup
/login
/me
/notes
/notes/<int:id>
```

---

## Authentication

The API uses JWT Authentication.

After logging in, copy the returned access token and include it in every protected request.

Example

```
Authorization: Bearer YOUR_TOKEN
```

---

## Testing

The following functionality was successfully tested.

- User registration
- Duplicate username validation
- User login
- JWT token generation
- Protected routes
- Get current user
- Create note
- View notes
- Update note
- Delete note
- Database migrations
- Database seeding

---

## Author

Brian Kipkoech

GitHub

https://github.com/kipkoechbrian-dot