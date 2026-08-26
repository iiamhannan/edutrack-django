from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

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
]
