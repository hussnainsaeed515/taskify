# Taskify API

A production-style Task Management REST API built with FastAPI, featuring JWT authentication and PostgreSQL database integration.
## Live Demo
🔗 [https://taskify-8cj7.onrender.com/docs](https://taskify-8cj7.onrender.com/docs)

## Features

- 🔐 User authentication (Signup/Login) with JWT tokens
- 🔒 Password hashing using bcrypt
- ✅ Full CRUD operations for tasks (Create, Read, Update, Delete)
- 🛡️ Protected routes requiring authentication
- 🗄️ PostgreSQL database with SQLAlchemy ORM
- 🔄 Database migrations with Alembic

## Tech Stack

- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Migrations:** Alembic
- **Authentication:** JWT (PyJWT), bcrypt
- **Validation:** Pydantic

## API Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|--------------|----------------|
| POST | `/auth/signup` | Register new user | No |
| POST | `/auth/login` | Login and get token | No |
| POST | `/tasks` | Create a new task | Yes |
| GET | `/tasks` | Get all tasks | No |
| PUT | `/tasks/{id}` | Update a task | No |
| DELETE | `/tasks/{id}` | Delete a task | No |

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/hussnainsaeed515/taskify.git
cd taskify
```

2. Install dependencies
```bash
poetry install
```

3. Set up environment variables (create a `.env` file)

DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key


4. Run database migrations
```bash
poetry run alembic upgrade head
```

5. Start the server
```bash
poetry run uvicorn app.main:app --reload
```

6. Visit `http://127.0.0.1:8000/docs` for interactive API documentation

## Author

Hussnain Saeed