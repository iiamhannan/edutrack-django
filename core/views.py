from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Course, Department
from .forms import CourseForm, DepartmentForm


# ---------- Dashboard (placeholder — grows in later commits) ----------
class HomeView(LoginRequiredMixin, ListView):
    template_name = "core/home.html"
    model = Department
    context_object_name = "departments"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["course_count"] = Course.objects.count()
        ctx["department_count"] = Department.objects.count()
        return ctx


# ---------- Course CRUD ----------
class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "core/course_list.html"
    context_object_name = "courses"
    paginate_by = 10


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = "core/course_form.html"
    success_url = reverse_lazy("core:course-list")


class CourseUpdateView(LoginRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = "core/course_form.html"
    success_url = reverse_lazy("core:course-list")


class CourseDeleteView(LoginRequiredMixin, DeleteView):
    model = Course
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:course-list")


# ---------- Department CRUD ----------
class DepartmentListView(LoginRequiredMixin, ListView):
    model = Department
    template_name = "core/department_list.html"
    context_object_name = "departments"


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = "core/department_form.html"
    success_url = reverse_lazy("core:department-list")


class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = "core/department_form.html"
    success_url = reverse_lazy("core:department-list")


class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Department
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:department-list")
