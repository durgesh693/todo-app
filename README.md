# Flask To-Do App

A small task-management web application built with Flask, Flask-SQLAlchemy, SQLite, HTML, and CSS. It is intended as a learning project and demonstrates Flask blueprints, sessions, forms, flash messages, and database-backed task management.

## Features

- Demo login and logout using Flask sessions
- Add tasks to a SQLite database
- Cycle a task through `pending`, `working`, and `done` statuses
- Clear all saved tasks
- Flash messages for login, logout, task creation, and status changes
- Responsive, simple HTML/CSS interface

## Project Structure

```text
todo-app/
├── app/
│   ├── routes/
│   │   ├── auth.py          # Login and logout routes
│   │   └── tasks.py         # Task routes and database actions
│   ├── static/
│   │   ├── css/style.css    # Application styles
│   │   └── js/script.js     # JavaScript entry file
│   ├── templates/           # Jinja HTML templates
│   ├── __init__.py          # Flask application factory and configuration
│   └── models.py            # SQLAlchemy task model
├── instance/                # Local SQLite database location (not committed)
├── run.py                   # Application entry point
└── requirements.txt         # Python dependencies
```

## Requirements

- Python 3.10 or newer
- pip

## Installation

Create and activate a virtual environment:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Run the App

```powershell
python run.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser. The SQLite database and tables are created automatically on first run.

## Demo Login

The application currently uses a demo login defined in `app/routes/auth.py`.
For safety, replace the hard-coded credentials with a proper user model and
hashed passwords before sharing or deploying the app.

## Current Limitations

This is a learning project. Before deploying it publicly, improve the following areas:

- Replace the hard-coded secret key and demo credentials with environment variables and hashed user passwords.
- Add a user model and associate each task with its owner.
- Require authentication for every task-changing endpoint, including status changes and clearing tasks.
- Add CSRF protection, tests, database migrations, and production configuration.
- Complete the registration flow, which currently only has a placeholder template.

## Git Notes

The `.gitignore` excludes virtual environments, Python caches, environment files, and local SQLite database files. This keeps machine-specific data out of the repository.
