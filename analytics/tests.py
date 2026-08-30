from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from core.models import Course, Department, Enrollment, Grade, Student


class AnalyticsDashboardTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser("admin", "admin@example.com", "adminpass123")
        self.client.login(username="admin", password="adminpass123")

    def test_dashboard_loads_with_no_data(self):
        """The dashboard should not crash even when there are no grades/attendance yet."""
        response = self.client.get(reverse("analytics:dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_loads_with_data(self):
        department = Department.objects.create(name="Computer Science")
        course = Course.objects.create(code="CS101", title="Intro to Programming", credit_hours=3, department=department)
        student = Student.objects.create(
            roll_no="CS-001", first_name="Ali", last_name="Khan",
            email="ali@example.com", department=department,
        )
        enrollment = Enrollment.objects.create(student=student, course=course, semester=1)
        Grade.objects.create(enrollment=enrollment, marks_obtained=92)

        response = self.client.get(reverse("analytics:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("charts", response.context)
        self.assertTrue(response.context["has_grade_data"])
