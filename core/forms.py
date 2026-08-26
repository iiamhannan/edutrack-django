from django import forms
from .models import Course, Department


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
