# EduTrack – Student Management & Analytics System

A Django-based Student Management System with an analytics dashboard (Pandas/NumPy/Matplotlib)
for tracking students, courses, enrollments, attendance, and grades.

> 🚧 **Work in progress.** This commit adds the `core` app with **Department**
> and **Course** management (full CRUD), the foundation the rest of the
> system builds on. More features are added incrementally in the commits
> that follow.

## Features so far
- Department CRUD (list, add, edit, delete)
- Course CRUD, linked to a Department
- Dashboard showing department/course counts

## Tech Stack
- Python, Django
- Bootstrap 5 (UI)
- SQLite (default) / MySQL (optional, see settings)
- Pandas, NumPy, Matplotlib (for the analytics dashboard — coming soon)

## Setup

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Author
**Muhammad Hanan** — [GitHub](https://github.com/iiamhannan)
