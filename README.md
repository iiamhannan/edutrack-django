# EduTrack – Student Management & Analytics System
🔗 Live Demo: https://iiamhannan26.pythonanywhere.com

A full-featured **Student Management System** built with Django, featuring complete CRUD for
departments, courses, students, enrollments, attendance, and grades — plus an **analytics
dashboard** powered by Pandas, NumPy, and Matplotlib.

## Features

- 🔐 **Authentication** — login/logout, all views protected
- 🏫 **Departments** — CRUD
- 📚 **Courses** — CRUD, linked to a department
- 🎓 **Students** — CRUD with search (roll no, name, email) and pagination
- 📝 **Enrollments** — enroll students into courses per semester
- 📅 **Attendance** — mark present / absent / leave per enrollment
- 🏆 **Grades** — record marks, auto-calculated letter grade (A–F)
- 📊 **Analytics Dashboard**
  - Average marks per course (bar chart)
  - Grade distribution (pie chart)
  - Top 5 students by average marks
  - Attendance % per course
  - All computed with **Pandas** + **NumPy**, rendered with **Matplotlib**
- 🌱 **Demo data seeding** — one command populates realistic sample data
- ✅ **Unit tests** for core models, views, and the analytics dashboard

## Tech Stack

- **Backend:** Python, Django (class-based views)
- **Data/Analytics:** Pandas, NumPy, Matplotlib
- **Frontend:** Django Templates, Bootstrap 5, Bootstrap Icons
- **Database:** SQLite (default) — MySQL supported via environment variables

## Project Structure

```
edutrack/
├── sms_project/         # Project settings & root URL config
├── core/                 # Departments, Courses, Students, Enrollments, Attendance, Grades
│   ├── management/commands/seed_data.py   # Demo data generator
│   ├── models.py, views.py, forms.py, urls.py, admin.py
│   └── templates/core/
├── analytics/            # Pandas/NumPy/Matplotlib dashboard
│   ├── views.py
│   └── templates/analytics/dashboard.html
├── templates/             # Base template, login page
├── static/css/style.css
├── requirements.txt
└── manage.py
```

## Setup & Installation

```bash
# 1. Clone the repo
git clone https://github.com/iiamhannan/edutrack-django.git
cd edutrack-django

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment variables
cp .env.example .env

# 5. Run migrations
python manage.py migrate

# 6. Seed demo data (creates an admin user: admin / admin123, plus sample
#    departments, courses, students, enrollments, attendance and grades)
python manage.py seed_data --students 25

# 7. Run the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` and log in with **admin / admin123** (or your own
`createsuperuser` account).

- App: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`
- Analytics dashboard: `http://127.0.0.1:8000/analytics/`

## Using MySQL instead of SQLite

By default the project uses SQLite so it runs with zero setup. To use MySQL:

```bash
pip install mysqlclient
```

Then set these environment variables (in `.env`):

```
SMS_USE_MYSQL=True
DB_NAME=sms_db
DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=127.0.0.1
DB_PORT=3306
```

## Running Tests

```bash
python manage.py test
```

Covers: model behavior (letter grade calculation, full name), authentication-gated
views, student creation, and the analytics dashboard (with and without data).

## Future Improvements

- Role-based access (Admin / Teacher / Student logins)
- CSV/Excel export of grades and attendance
- Email notifications for low attendance
- REST API layer (Django REST Framework) for a mobile app

## Author

**Muhammad Hanan**
[GitHub](https://github.com/iiamhannan) · [LinkedIn](https://www.linkedin.com/in/muhammad-hanan-323bb9219)
