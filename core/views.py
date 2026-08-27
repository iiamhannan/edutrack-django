from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Course, Department, Student
from django.views.generic import DetailView
from .forms import CourseForm, DepartmentForm, StudentForm


# ---------- Dashboard (placeholder — grows in later commits) ----------
class HomeView(LoginRequiredMixin, ListView):
    template_name = "core/home.html"
    model = Student
    context_object_name = "recent_students"

    def get_queryset(self):
        return Student.objects.order_by("-enrollment_date")[:5]

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["student_count"] = Student.objects.count()
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


# ---------- Student CRUD ----------
class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    template_name = "core/student_list.html"
    context_object_name = "students"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related("department")
        q = self.request.GET.get("q")
        if q:
            from django.db.models import Q
            qs = qs.filter(
                Q(roll_no__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(email__icontains=q)
            )
        return qs


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    template_name = "core/student_detail.html"
    context_object_name = "student"


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = "core/student_form.html"
    success_url = reverse_lazy("core:student-list")


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "core/student_form.html"
    success_url = reverse_lazy("core:student-list")


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = "core/confirm_delete.html"
    success_url = reverse_lazy("core:student-list")
