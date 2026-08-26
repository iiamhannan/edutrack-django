# EduTrack – Student Management & Analytics System

A Django-based Student Management System with an analytics dashboard (Pandas/NumPy/Matplotlib)
for tracking students, courses, enrollments, attendance, and grades.

> 🚧 **Work in progress.** This commit sets up the base Django project structure
> (settings, base template, static files, authentication scaffold). Features
> will be added incrementally in the commits that follow.

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
