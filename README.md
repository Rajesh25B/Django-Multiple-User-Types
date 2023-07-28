# User-Types Django Project

A Django-based web application that demonstrates how to handle multiple database tables for users and orders. This project utilizes Docker and Docker Compose to manage the development environment and multiple database containers.

## Setup Instructions

### Prerequisites

Make sure you have the following software installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Clone the Repository

```bash
git clone https://github.com/your-username/User-Types.git
cd User-Types
```

### Environment Variables

Create a `.env` file in the root of the project and set the following environment variables for the database connections:

```plaintext
# Default database
DB_NAME=default_db
DB_USER=db_user
DB_PASSWORD=setyourdbpassword
DB_HOST=db
DB_PORT=5432
POSTGRES_PASSWORD=setyourdbpassword

# Users database
USERS_DB_NAME=users_db
USERS_DB_USER=users_db_user
USERS_DB_PASSWORD=setyourdbpassword
USERS_DB_HOST=users_db
USERS_DB_PORT=5432
USERS_POSTGRES_PASSWORD=setyourdbpassword

# Orders database
ORDERS_DB_NAME=orders_db
ORDERS_DB_USER=orders_db_user
ORDERS_DB_PASSWORD=setyourdbpassword
ORDERS_DB_HOST=orders_db
ORDERS_DB_PORT=5432
ORDERS_POSTGRES_PASSWORD=setyourdbpassword
```

### Running the Application

To run the User-Types application with Docker Compose, use the following command:

```bash
docker-compose up
```

This will start the Django development server and the required PostgreSQL database containers. You should be able to access the application at `http://localhost:8000/`.

### Accessing the Admin Panel

To access the Django Admin panel, create a superuser for the `default_db` database:

```bash
docker-compose run web python manage.py createsuperuser
```

Then, navigate to `http://localhost:8000/admin/` and log in using the superuser credentials.

### Database Configuration in Django

In the `settings.py` file of the Django project, you can find the database configurations for the default, users, and orders databases. Make sure to use the appropriate environment variables for the database settings as defined in the `.env` file.

## Contributing

Contributions to the User-Types project are welcome! Feel free to submit issues and pull requests for bug fixes, improvements, or new features.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify it for your needs.

---

Thank you for checking out the User-Types Django project! If you have any questions or need assistance, please don't hesitate to open an issue or contact us.

Happy coding!