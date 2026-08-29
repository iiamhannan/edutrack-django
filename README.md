# EduTrack – Student Management & Analytics System

A Django-based Student Management System with an analytics dashboard (Pandas/NumPy/Matplotlib)
for tracking students, courses, enrollments, attendance, and grades.

> 🚧 **Work in progress.** This commit adds the **Analytics Dashboard**
> (`/analytics/`), which uses Pandas + NumPy to compute grade/attendance
> statistics and Matplotlib to render charts (average marks per course,
> grade distribution, top students, attendance %). More features are added
> incrementally in the commits that follow.

## Features so far
- Department CRUD (list, add, edit, delete)
- Course CRUD, linked to a Department
- Student CRUD with search (by roll no, name, email) and pagination
- Enrollment system — enroll students into courses per semester
- Attendance tracking (present/absent/leave) per enrollment
- Grading system with auto-calculated letter grades
- **Analytics dashboard** — Pandas/NumPy stats + Matplotlib charts (average marks, grade distribution, top students, attendance %)
- Dashboard showing student/department/course/enrollment counts + recent students

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
