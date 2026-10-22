# To-Do List (Django)

A multi-user to-do list web app built with Django.

## Features

- **User accounts:** register and log in (`users_app`)
- **Task management:** add, edit, delete and mark tasks as completed or pending. Each user sees only their own tasks.
- **Extra pages:** Home, About, Contact and a Tic-Tac-Toe game

## Project structure

| Path | Purpose |
|------|---------|
| `first_project/` | Django project settings and root URLs |
| `first_app/` | To-do app: `TaskList` model, views, forms, templates and static files |
| `users_app/` | User registration and authentication |
| `templates/`, `static/` | Shared templates and assets |
| `db.sqlite3` | Development database |

## Getting started

```bash
pip install django
python manage.py migrate
python manage.py runserver
```

Then open http://127.0.0.1:8000. The task list is at `/todolist/`.
