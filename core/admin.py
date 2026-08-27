from django.contrib import admin
from .models import Department, Course


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["code", "title", "credit_hours", "department"]
    list_filter = ["department"]
    search_fields = ["code", "title"]


from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["roll_no", "first_name", "last_name", "department", "semester", "status"]
    list_filter = ["department", "status", "semester"]
    search_fields = ["roll_no", "first_name", "last_name", "email"]
