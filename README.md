# EduTrack – Student Management & Analytics System

A Django-based Student Management System with an analytics dashboard (Pandas/NumPy/Matplotlib)
for tracking students, courses, enrollments, attendance, and grades.

> 🚧 **Work in progress.** This commit adds full **Student management**
> (CRUD + search + pagination) and links students to departments. Dashboard
> now shows recently added students. More features are added incrementally
> in the commits that follow.

## Features so far
- Department CRUD (list, add, edit, delete)
- Course CRUD, linked to a Department
- Student CRUD with search (by roll no, name, email) and pagination
- Dashboard showing student/department/course counts + recent students

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
