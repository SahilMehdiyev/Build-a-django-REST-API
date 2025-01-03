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
