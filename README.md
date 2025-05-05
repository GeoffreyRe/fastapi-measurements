# FastAPI Measurements API

A Dockerized API built with **FastAPI**, using **SQLAlchemy** and a **PostgreSQL** database.

## ✅ Prerequisites

To use this project, you need:

- Basic knowledge of Git and GitHub
- Docker installed and a basic understanding of how to use it

## 📦 Project Description

This project is an API developed using:

- **FastAPI** for the web framework
- **SQLAlchemy** for ORM (Object Relational Mapping)
- **PostgreSQL** for data persistence
- Fully containerized with **Docker** and **docker-compose**

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1. Clone the repository (example with HTTPS)

```bash
git clone https://github.com/GeoffreyRe/fastapi-measurements.git
```

### 2. Create a `.env` file

Inside the `/docker` folder, create a `.env` file with the following variables:

```env
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
```

### 3. Build and run the Docker containers

Navigate inside /docker folder and run the following command :

```bash
docker compose up -d --build
```

This command will launch the web application.


### 4. Access the API

Once the containers are up and running, the API is available at:

```
http://localhost:8000
```

## 📚 API Documentation

You can explore the automatically generated interactive documentation at:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 🧪 Running Tests

To run the tests, execute this command when the containers are up:

```bash
docker exec -it fastapi-measurements-backend pytest /app/tests/
```

To run the tests with coverage report:

```bash
docker exec -it fastapi-measurements-backend pytest --cov=app /app/tests/
```

## 🔮 Next Steps

Here are some ideas for future improvements to this project:

- **Add migrations with Alembic**  
  Implement database schema migrations using [Alembic](https://alembic.sqlalchemy.org/) for better control over schema changes.

- **Improve test coverage and robustness**  
  - Add more test cases for edge scenarios (e.g., missing or invalid fields in requests)
  - Test error responses and validation logic

- **Add authentication system**  
  Implement user authentication using OAuth2 with JWT tokens to secure endpoints.

- **Enhance filtering capabilities on GET /measurements**  
  Add query parameters to filter measurements, such as:
  - Filter by `time` range (e.g., `?start=2024-01-01&end=2024-02-01`)
  - Filter by `unit_id` or other attributes

## 👤 Author

Geoffrey Remacle