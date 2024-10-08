# Fitness Center Management Information System (fitnessCenterMIS)

This is a Flask-based web application designed to manage customer services for fitness centers. It allows administrators to manage fitness centers, services, trainers, schedules, and client orders. Clients can browse services, schedule sessions, and post reviews for trainers. The project uses **SQLAlchemy** for ORM, **Alembic** for database migrations, **Celery** for background tasks, and Docker Compose for easy deployment.

The project can be easily extended to other service-based businesses like spas, salons, healthcare centers, and more.

## Features

### User Types:
1. **Admin**
   - Add and manage fitness centers.
   - Assign services and trainers to fitness centers.
   - Define and manage trainer schedules.
   - View client bookings and reviews.

2. **Client**
   - Browse fitness centers and available services.
   - Select a service and trainer.
   - Schedule an appointment with a trainer.
   - Post reviews for trainers.

### Core Entities:
- **Client**: Represents a user who can book services and post reviews.
- **Fitness Center**: The business entity offering various services and trainers.
- **Service**: Represents different types of fitness or wellness services (e.g., Yoga, Weight Training, etc.).
- **Trainer**: Represents fitness trainers assigned to specific services.
- **Order**: Represents a client's booking for a service.
- **Schedule**: Defines the availability of a trainer for a specific service.
- **Review**: Client feedback for a trainer after availing of the service.

### Database Support:
The project supports both:
- **SQLite** for local development and testing.
- **PostgreSQL** for production environments.

### Additional Features:
- **User Registration Messages**: After a user registers, a background task sends a confirmation message via **Celery** and **RabbitMQ**.
- **Database Migrations**: Manage database schema changes using **Alembic** with **SQLAlchemy**.
- **Containerized Application**: Dockerized for easy setup and deployment with **Docker Compose** or standalone Docker commands.

## Installation

### Prerequisites
- Python 3.x
- Flask
- SQLAlchemy
- Alembic
- Celery
- RabbitMQ
- PostgreSQL
- Docker & Docker Compose

## Running the Application with Docker Compose

The project includes a `docker-compose.yml` file for running the application, Celery workers, RabbitMQ, and PostgreSQL database.

**Build and Start Containers:**
   ```bash
   docker-compose up --build
