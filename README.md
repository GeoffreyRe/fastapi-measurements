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

This **API** allows interaction with **CO₂ measurements**. It enables clients to store the amount of **CO₂** recorded at a specific point in time, along with metadata such as the unit, data source, and optional description. This is useful for **tracking environmental data** over time and **analyzing trends** in carbon emissions.

## 🚀 Getting Started

Follow these steps to run the project locally:

### 1. Clone the repository (example with HTTPS)

```bash
git clone https://github.com/GeoffreyRe/fastapi-measurements.git
```

### 2. Create a `.env` file

Inside the `/docker` folder, create a `.env` file with the following variables:

```env
SECRET_KEY=your_secret_key
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
ADMIN_USERNAME=your_admin_name
ADMIN_PASSWORD=your_admin_password
ADMIN_EMAIL=your_admin_email
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

## 📦 Database Migrations

This project uses [Alembic](https://alembic.sqlalchemy.org/) to manage database schema migrations.

To generate and apply migrations manually:

### 1. **Create a new revision:**

   ```bash
   docker exec -w /app -it fastapi-measurements-backend alembic revision --autogenerate -m "Your message"
   ```

### 2. **Apply the latest migrations:**

   ```bash
   docker exec -w /app -it fastapi-measurements-backend alembic upgrade head
   ```

### 3. **Rollback the latest migration:**

   ```bash
   docker exec -w /app -it fastapi-measurements-backend alembic downgrade -1
   ```

### 4. **Check the current revision:**

   ```bash
   docker exec -w /app -it fastapi-measurements-backend alembic current
   ```

## 🔮 Next Steps

Here are some ideas for future improvements to this project:

- **Improve test coverage and robustness**  
  - Add more test cases for edge scenarios (e.g., missing or invalid fields in requests)
  - Test error responses and validation logic

- **Add authentication system**  
  Implement user authentication using OAuth2 with JWT tokens to secure endpoints.
 
- **Enhance filtering capabilities on GET /measurements**  
  Add query parameters to filter measurements, such as:
  - Filter by `time` range (e.g., `?start=2024-01-01&end=2024-02-01`)

## 👤 Author

Geoffrey Remacle