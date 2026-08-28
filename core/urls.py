from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    # Students
    path("students/", views.StudentListView.as_view(), name="student-list"),
    path("students/add/", views.StudentCreateView.as_view(), name="student-add"),
    path("students/<int:pk>/", views.StudentDetailView.as_view(), name="student-detail"),
    path("students/<int:pk>/edit/", views.StudentUpdateView.as_view(), name="student-edit"),
    path("students/<int:pk>/delete/", views.StudentDeleteView.as_view(), name="student-delete"),

    # Enrollments
    path("enrollments/", views.EnrollmentListView.as_view(), name="enrollment-list"),
    path("enrollments/add/", views.EnrollmentCreateView.as_view(), name="enrollment-add"),
    path("enrollments/<int:pk>/delete/", views.EnrollmentDeleteView.as_view(), name="enrollment-delete"),

    # Courses
    path("courses/", views.CourseListView.as_view(), name="course-list"),
    path("courses/add/", views.CourseCreateView.as_view(), name="course-add"),
    path("courses/<int:pk>/edit/", views.CourseUpdateView.as_view(), name="course-edit"),
    path("courses/<int:pk>/delete/", views.CourseDeleteView.as_view(), name="course-delete"),

    # Departments
    path("departments/", views.DepartmentListView.as_view(), name="department-list"),
    path("departments/add/", views.DepartmentCreateView.as_view(), name="department-add"),
    path("departments/<int:pk>/edit/", views.DepartmentUpdateView.as_view(), name="department-edit"),
    path("departments/<int:pk>/delete/", views.DepartmentDeleteView.as_view(), name="department-delete"),

    # Attendance
    path("attendance/", views.AttendanceListView.as_view(), name="attendance-list"),
    path("attendance/add/", views.AttendanceCreateView.as_view(), name="attendance-add"),
    path("attendance/<int:pk>/delete/", views.AttendanceDeleteView.as_view(), name="attendance-delete"),

    # Grades
    path("grades/", views.GradeListView.as_view(), name="grade-list"),
    path("grades/add/", views.GradeCreateView.as_view(), name="grade-add"),
    path("grades/<int:pk>/edit/", views.GradeUpdateView.as_view(), name="grade-edit"),
    path("grades/<int:pk>/delete/", views.GradeDeleteView.as_view(), name="grade-delete"),
]
