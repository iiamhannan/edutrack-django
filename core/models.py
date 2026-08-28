from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Course(models.Model):
    code = models.CharField(max_length=15, unique=True)
    title = models.CharField(max_length=150)
    credit_hours = models.PositiveSmallIntegerField(default=3)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="courses"
    )

    class Meta:
        ordering = ["code"]

    def __str__(self):
        return f"{self.code} - {self.title}"

    def get_absolute_url(self):
        return reverse("core:course-list")


class Student(models.Model):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("graduated", "Graduated"),
        ("suspended", "Suspended"),
    ]
    roll_no = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, related_name="students"
    )
    semester = models.PositiveSmallIntegerField(default=1)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="active")
    enrollment_date = models.DateField(auto_now_add=True)
    courses = models.ManyToManyField(Course, through="Enrollment", related_name="students")

    class Meta:
        ordering = ["roll_no"]

    def __str__(self):
        return f"{self.roll_no} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("core:student-detail", args=[self.pk])


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    semester = models.PositiveSmallIntegerField(default=1)
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course", "semester")
        ordering = ["-date_enrolled"]

    def __str__(self):
        return f"{self.student.roll_no} -> {self.course.code}"


class Attendance(models.Model):
    STATUS_CHOICES = [("present", "Present"), ("absent", "Absent"), ("leave", "Leave")]
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="present")

    class Meta:
        ordering = ["-date"]
        unique_together = ("enrollment", "date")

    def __str__(self):
        return f"{self.enrollment} - {self.date} - {self.status}"


class Grade(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE, related_name="grade")
    marks_obtained = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        ordering = ["-marks_obtained"]

    def __str__(self):
        return f"{self.enrollment} - {self.marks_obtained}"

    @property
    def letter_grade(self):
        m = float(self.marks_obtained)
        if m >= 85:
            return "A"
        elif m >= 70:
            return "B"
        elif m >= 60:
            return "C"
        elif m >= 50:
            return "D"
        return "F"
