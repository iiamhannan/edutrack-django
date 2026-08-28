from django import forms
from .models import Course, Department, Student, Enrollment, Attendance, Grade


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["code", "title", "credit_hours", "department"]
        widgets = {
            "code": forms.TextInput(attrs={"class": "form-control"}),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "credit_hours": forms.NumberInput(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-select"}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control"})}


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["roll_no", "first_name", "last_name", "email", "phone", "department", "semester", "status"]
        widgets = {
            "roll_no": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "department": forms.Select(attrs={"class": "form-select"}),
            "semester": forms.NumberInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ["student", "course", "semester"]
        widgets = {
            "student": forms.Select(attrs={"class": "form-select"}),
            "course": forms.Select(attrs={"class": "form-select"}),
            "semester": forms.NumberInput(attrs={"class": "form-control"}),
        }


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ["enrollment", "date", "status"]
        widgets = {
            "enrollment": forms.Select(attrs={"class": "form-select"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ["enrollment", "marks_obtained"]
        widgets = {
            "enrollment": forms.Select(attrs={"class": "form-select"}),
            "marks_obtained": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
        }
