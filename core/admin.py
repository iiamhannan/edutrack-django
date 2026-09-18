from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html

from .models import Attendance, Course, Department, Enrollment, Grade, Student

# ---------------------------------------------------------------------------
# Site branding
# ---------------------------------------------------------------------------
admin.site.site_header = "EduTrack Administration"
admin.site.site_title = "EduTrack Admin"
admin.site.index_title = "Records overview"


def badge(text, css_class):
    """Render a small coloured text pill. No icons/emoji — text only."""
    return format_html('<span class="et-badge {}">{}</span>', css_class, text)


# ---------------------------------------------------------------------------
# Department
# ---------------------------------------------------------------------------
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "course_count", "student_count"]
    search_fields = ["name"]
    ordering = ["name"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_course_count=Count("courses", distinct=True),
                            _student_count=Count("students", distinct=True))

    @admin.display(description="Courses", ordering="_course_count")
    def course_count(self, obj):
        return obj._course_count

    @admin.display(description="Students", ordering="_student_count")
    def student_count(self, obj):
        return obj._student_count


# ---------------------------------------------------------------------------
# Course
# ---------------------------------------------------------------------------
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["code", "title", "credit_hours", "department", "enrolled_count"]
    list_filter = ["department", "credit_hours"]
    search_fields = ["code", "title"]
    autocomplete_fields = ["department"]
    list_select_related = ["department"]
    ordering = ["code"]
    list_per_page = 25
    fieldsets = (
        ("Course details", {"fields": ("code", "title", "credit_hours", "department")}),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_enrolled_count=Count("enrollments", distinct=True))

    @admin.display(description="Enrolled", ordering="_enrolled_count")
    def enrolled_count(self, obj):
        return obj._enrolled_count


# ---------------------------------------------------------------------------
# Student
# ---------------------------------------------------------------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["roll_no", "name_with_email", "department", "semester", "status_display"]
    list_filter = ["department", "status", "semester"]
    search_fields = ["roll_no", "first_name", "last_name", "email"]
    autocomplete_fields = ["department"]
    list_select_related = ["department"]
    readonly_fields = ["enrollment_date"]
    date_hierarchy = "enrollment_date"
    ordering = ["roll_no"]
    list_per_page = 25
    save_on_top = True

    fieldsets = (
        ("Identity", {
            "fields": ("roll_no", "first_name", "last_name", "email", "phone"),
        }),
        ("Academic record", {
            "fields": ("department", "semester", "status", "enrollment_date"),
        }),
    )

    @admin.display(description="Student", ordering="first_name")
    def name_with_email(self, obj):
        return format_html(
            "{}<span class=\"et-subtext\">{}</span>",
            obj.full_name,
            obj.email,
        )

    @admin.display(description="Status", ordering="status")
    def status_display(self, obj):
        css = {"active": "status-active", "graduated": "status-graduated",
               "suspended": "status-suspended"}.get(obj.status, "")
        return badge(obj.get_status_display(), css)


# ---------------------------------------------------------------------------
# Enrollment
# ---------------------------------------------------------------------------
@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ["student", "course", "semester", "date_enrolled"]
    list_filter = ["semester", "course", "date_enrolled"]
    search_fields = [
        "student__roll_no", "student__first_name", "student__last_name",
        "course__code", "course__title",
    ]
    autocomplete_fields = ["student", "course"]
    list_select_related = ["student", "course"]
    date_hierarchy = "date_enrolled"
    ordering = ["-date_enrolled"]
    list_per_page = 25


# ---------------------------------------------------------------------------
# Attendance
# ---------------------------------------------------------------------------
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["enrollment", "date", "status_display"]
    list_filter = ["status", "date"]
    search_fields = [
        "enrollment__student__roll_no", "enrollment__student__first_name",
        "enrollment__student__last_name", "enrollment__course__code",
    ]
    autocomplete_fields = ["enrollment"]
    list_select_related = ["enrollment", "enrollment__student", "enrollment__course"]
    date_hierarchy = "date"
    ordering = ["-date"]
    list_per_page = 25

    @admin.display(description="Status", ordering="status")
    def status_display(self, obj):
        css = {"present": "attend-present", "absent": "attend-absent",
               "leave": "attend-leave"}.get(obj.status, "")
        return badge(obj.get_status_display(), css)


# ---------------------------------------------------------------------------
# Grade
# ---------------------------------------------------------------------------
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["enrollment", "marks_obtained", "letter_grade_display"]
    list_filter = ["enrollment__course"]
    search_fields = [
        "enrollment__student__roll_no", "enrollment__student__first_name",
        "enrollment__student__last_name", "enrollment__course__code",
    ]
    autocomplete_fields = ["enrollment"]
    list_select_related = ["enrollment", "enrollment__student", "enrollment__course"]
    ordering = ["-marks_obtained"]
    list_per_page = 25

    @admin.display(description="Grade")
    def letter_grade_display(self, obj):
        grade = obj.letter_grade
        return badge(grade, f"grade-{grade}")
