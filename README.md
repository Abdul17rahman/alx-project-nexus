# ALX Project Nexus — Job Board Backend

Welcome to **alx-project-nexus**, the documentation and codebase hub for the Job Board Backend built as part of the **ProDev Backend Engineering** program. This project demonstrates my understanding of backend engineering concepts such as authentication, role-based access control, efficient data modeling, and API development.

---

## Project Overview

This backend system powers a **Job Board Platform**, enabling:

- Posting and categorizing jobs
- User and admin role management
- Efficient job search/filtering
- Token-based authentication (JWT)
- Fully documented APIs (Swagger)

---

## Technologies Used

| Technology                          | Purpose                                 |
| ----------------------------------- | --------------------------------------- |
| Django                              | Web framework for backend development   |
| Django REST Framework               | RESTful API creation                    |
| PostgreSQL                          | Relational database                     |
| JWT (djangorestframework-simplejwt) | Secure authentication                   |
| Swagger (drf-yasg)                  | Interactive API documentation           |
| Docker                              | Containerization for environment parity |
| Git + GitHub                        | Version control and collaboration       |

---

### Key Features

#### 1. Job Posting Management

- Create, update, delete, and retrieve job listings
- Categorize jobs by **industry**, **location**, and **type**

#### 2. Role-Based Access Control

- **Admin** users: Manage jobs and categories
- **Regular** users: Apply for jobs and track applications
- Authentication via **JWT**

#### 3. Optimized Job Search

- Index-based querying for fast results
- Location-based and category-based filters

### 4 Swagger API Documentation

- Live docs at `/api/swagger/`
- Auto-generated from viewsets and serializers
- Custom tags, descriptions, and error formats

#### 5. API Documentation

- **URL**: `http://localhost:8000/api/docs/`
- **Auth**: JWT Bearer Token (`Authorization: Bearer <token>`)

Sample Endpoints:

| Method | Endpoint           | Description                |
| ------ | ------------------ | -------------------------- |
| GET    | /api/jobs/         | List all jobs              |
| POST   | /api/jobs/         | Create a job (admin only)  |
| POST   | /api/token/        | Login & receive tokens     |
| GET    | /api/applications/ | View user job applications |

---

## Challenges & Solutions

| Challenge                     | Solution                                                 |
| ----------------------------- | -------------------------------------------------------- |
| Implementing secure RBAC      | Used Django’s `permissions` + JWT                        |
| Efficient job filtering       | Applied PostgreSQL indexing and Django ORM optimizations |
| Documenting APIs              | Integrated `drf-yasg` to auto-generate Swagger docs      |
| Managing different user roles | Custom user model and permission classes                 |

---

## Best Practices & Takeaways

- Write modular, reusable code
- Prioritize security: validate input, sanitize data, use HTTPS
- Keep APIs well-documented and testable
- Design with scalability and performance in mind
- CI/CD ensures safe and fast deployment cycles

---

## Database Design Overview

Tables:

    User – Custom user model

    JobCategory – Categories for jobs (e.g., IT, Healthcare)

    JobType – Types like Full-time, Part-time, Remote

    Location – Cities or regions for job location

    Job – Actual job postings

    Application – User-submitted job applications

    Company – Company profiles

---

## Repository Setup Instructions

1.  Clone this repository:

    ```bash
    git clone https://github.com/<your-username>/alx-project-nexus.git
    ```

2.  Navigate into the folder:

    ```bash
    cd alx-project-nexus
    ```

3.  Create a Virtual Environment
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
4.  Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
5.  Set Up Environment Variables

    Create a .env file in the root directory and add:

    SECRET_KEY=your-django-secret-key
    DEBUG=True
    ALLOWED_HOSTS=127.0.0.1,localhost
    DATABASE_NAME=jobboard
    DATABASE_USER=your_db_user
    DATABASE_PASSWORD=your_db_password
    DATABASE_HOST=localhost
    DATABASE_PORT=5432

6.  Configure the Database
    Ensure PostgreSQL is running and a database is created:

        ```sql
        CREATE DATABASE jobboard;
        ```

7.  Run Migrations

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

8.  Create Superuser

    ```bash
    python manage.py createsuperuser
    ```

9.  Run the Server

    ```bash
    python manage.py runserver
    ```

10. Access the API Docs
    Visit: http://127.0.0.1:8000/api/docs on your favourite browser to access the app.

## Docker Setup

    You can run the project inside containers using Docker Compose.

1. Build and Run Containers
   ```bash
   docker-compose up --build
   ```
2. Access the App

   API: http://localhost:8000/

## Project Structure

alx-project-nexus/

    ├── jobboard/
    │ ├── settings.py
    │ ├── urls.py
    │ └── wsgi.py
    │
    ├── jobs/
    │ ├── models.py
    │ ├── serializers.py
    │ ├── views.py
    │ ├── permissions.py
    │ └── urls.py
    │
    ├── applications/
    │ ├── models.py
    │ ├── serializers.py
    │ ├── views.py
    │ └── urls.py
    │
    ├── users/
    │ ├── models.py
    │ ├── serializers.py
    │ ├── views.py
    │ └── urls.py
    │
    ├── requirements.txt
    ├── docker-compose.yml
    ├── .env
    └── README.md

## Author

Abdul Rahman
Backend Engineer • ALX ProDev Graduate
GitHub: @Abdul17rahman

## License

This project is licensed under the MIT License.
