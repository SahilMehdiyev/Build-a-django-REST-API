# DRF Project

## 📚 Overview
This project is built using Django and Django REST Framework (DRF) to provide a robust and scalable backend solution. The project also incorporates modern tools and configurations to streamline development, testing, and deployment processes.

## 🚀 Features
- **Django REST Framework**: To handle API endpoints.
- **Pre-commit Hooks**: Ensures code quality before commits.
- **Relational Models**: Fully configured models for `api`, `cfhome`, `products`, `py_client`, and `search`.
- **Makefile**: Automates routine tasks like migrations, server start, and testing.
- **Database Support**: SQLite3 configured out-of-the-box.
- **Poetry for Dependency Management**: Simplifies package management and virtual environment handling.
- **Scalable Structure**: Modular app design for better scalability and maintainability.

---

## 🛠️ Tools and Technologies Used
### Backend Framework
- **Django**: Python web framework for rapid development.
- **Django REST Framework (DRF)**: For building RESTful APIs.

### Development Tools
- **Poetry**: Dependency and environment management.
- **Pre-commit**: Enforces code quality checks like formatting (Black) and linting (Flake8).

### Database
- **SQLite3**: Lightweight relational database.

### Others
- **Makefile**: For automating tasks.
- **Python 3.12**: Latest stable Python version for development.

---

## 🏗️ Project Structure
```plaintext
├── api/                  # API-related functionality
├── cfhome/               # Core configuration and home app
├── products/             # Product-related logic
├── py_client/            # Client and user management
├── search/               # Search functionality
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database file
├── Makefile              # Automation for tasks
├── poetry.lock           # Locked dependencies for Poetry
├── pyproject.toml        # Poetry configuration file
├── .gitignore            # Git ignore rules
└── README.md             # Project documentation



## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SahilMehdiyev/Build-a-django-REST-API.git
   cd Build-a-django-REST-API
   ```

2. **Install dependencies using Poetry**:
   ```bash
   poetry install
   ```

3. **Set up the environment**:
   - Create a `.env` file in the project root directory and add necessary environment variables.
   - Refer to `.env.example` for guidance.

4. **Run Docker containers**:
   Use Docker to start required services like the database:
   ```bash
   docker-compose up -d
   ```

5. **Apply database migrations**:
   ```bash
   poetry run python manage.py migrate
   ```

6. **Create a superuser** (optional, for accessing the Django admin interface):
   ```bash
   poetry run python manage.py createsuperuser
   ```

7. **Start the development server**:
   ```bash
   poetry run python manage.py runserver
   ```

---

## Usage

Once the server is running, you can:

- Access API endpoints to interact with the system.
- Test CRUD operations on various models like `products` and `search`.
- Use the Django admin interface for management.

---

```

Ensure all services are running before executing tests.

---

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, feel free to:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

Please ensure your contributions align with the project's goals and maintain clean, modular code.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions, suggestions, or feedback, feel free to reach out:

- **Author**: Sahil Mehdiyev
- **GitHub**: [SahilMehdiyev](https://github.com/SahilMehdiyev)

---

Happy building your APIs! 🚀




