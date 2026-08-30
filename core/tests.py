from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Course, Department, Enrollment, Grade, Student


class CoreModelTests(TestCase):
    def setUp(self):
        self.department = Department.objects.create(name="Computer Science")
        self.course = Course.objects.create(
            code="CS101", title="Intro to Programming", credit_hours=3, department=self.department
        )
        self.student = Student.objects.create(
            roll_no="CS-001", first_name="Ali", last_name="Khan",
            email="ali@example.com", department=self.department,
        )

    def test_student_full_name(self):
        self.assertEqual(self.student.full_name, "Ali Khan")

    def test_grade_letter_grade(self):
        enrollment = Enrollment.objects.create(student=self.student, course=self.course, semester=1)
        grade = Grade.objects.create(enrollment=enrollment, marks_obtained=88)
        self.assertEqual(grade.letter_grade, "A")

    def test_grade_letter_grade_fail(self):
        enrollment = Enrollment.objects.create(student=self.student, course=self.course, semester=1)
        grade = Grade.objects.create(enrollment=enrollment, marks_obtained=35)
        self.assertEqual(grade.letter_grade, "F")


class CoreViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser("admin", "admin@example.com", "adminpass123")
        self.client.login(username="admin", password="adminpass123")
        self.department = Department.objects.create(name="Computer Science")

    def test_home_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 302)  # redirected to login

    def test_home_loads_for_logged_in_user(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)

    def test_student_list_view(self):
        response = self.client.get(reverse("core:student-list"))
        self.assertEqual(response.status_code, 200)

    def test_create_student(self):
        response = self.client.post(reverse("core:student-add"), {
            "roll_no": "CS-002", "first_name": "Sara", "last_name": "Ahmed",
            "email": "sara@example.com", "phone": "", "department": self.department.id,
            "semester": 1, "status": "active",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Student.objects.filter(roll_no="CS-002").exists())
