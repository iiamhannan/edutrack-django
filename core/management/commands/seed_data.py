import random
from datetime import timedelta

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone

from core.models import Department, Course, Student, Enrollment, Attendance, Grade

FIRST_NAMES = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal", "Hassan", "Zainab", "Usman",
               "Fatima", "Hamza", "Mariam", "Omar", "Sana", "Kamran", "Nida", "Tariq"]
LAST_NAMES = ["Khan", "Malik", "Butt", "Chaudhry", "Raza", "Iqbal", "Shah", "Farooq",
              "Aslam", "Javed", "Qureshi", "Sheikh"]

DEPARTMENTS = ["Computer Science", "Data Science", "Software Engineering", "Business Administration"]

COURSES = [
    ("CS101", "Introduction to Programming", 3, "Computer Science"),
    ("CS201", "Data Structures & Algorithms", 4, "Computer Science"),
    ("DS101", "Statistics for Data Science", 3, "Data Science"),
    ("DS201", "Machine Learning Fundamentals", 4, "Data Science"),
    ("SE101", "Software Engineering Principles", 3, "Software Engineering"),
    ("BA101", "Principles of Management", 3, "Business Administration"),
]


class Command(BaseCommand):
    help = "Seeds the database with demo departments, courses, students, enrollments, attendance and grades."

    def add_arguments(self, parser):
        parser.add_argument("--students", type=int, default=25, help="Number of students to create")

    def handle(self, *args, **options):
        n_students = options["students"]

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "admin123")
            self.stdout.write(self.style.SUCCESS("Created superuser: admin / admin123"))

        dept_objs = {}
        for name in DEPARTMENTS:
            dept, _ = Department.objects.get_or_create(name=name)
            dept_objs[name] = dept

        course_objs = []
        for code, title, hours, dept_name in COURSES:
            course, _ = Course.objects.get_or_create(
                code=code, defaults={"title": title, "credit_hours": hours, "department": dept_objs[dept_name]}
            )
            course_objs.append(course)

        students = []
        for i in range(1, n_students + 1):
            roll_no = f"BSCS-{2024}{i:03d}"
            if Student.objects.filter(roll_no=roll_no).exists():
                continue
            fname = random.choice(FIRST_NAMES)
            lname = random.choice(LAST_NAMES)
            student = Student.objects.create(
                roll_no=roll_no,
                first_name=fname,
                last_name=lname,
                email=f"{fname.lower()}.{lname.lower()}{i}@example.com",
                phone=f"03{random.randint(00,99):02d}{random.randint(1000000,9999999)}",
                department=random.choice(list(dept_objs.values())),
                semester=random.randint(1, 8),
                status="active",
            )
            students.append(student)

        all_students = list(Student.objects.all())
        today = timezone.now().date()

        for student in all_students:
            enrolled_courses = random.sample(course_objs, k=random.randint(2, 4))
            for course in enrolled_courses:
                enrollment, created = Enrollment.objects.get_or_create(
                    student=student, course=course, semester=student.semester
                )
                if not created:
                    continue

                Grade.objects.get_or_create(
                    enrollment=enrollment,
                    defaults={"marks_obtained": round(random.uniform(40, 100), 2)},
                )

                for day_offset in range(10):
                    date = today - timedelta(days=day_offset * 3)
                    status = random.choices(
                        ["present", "absent", "leave"], weights=[80, 15, 5]
                    )[0]
                    Attendance.objects.get_or_create(
                        enrollment=enrollment, date=date, defaults={"status": status}
                    )

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {len(dept_objs)} departments, {len(course_objs)} courses, "
            f"{len(all_students)} students with enrollments, attendance and grades."
        ))
