import base64
from io import BytesIO

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from core.models import Grade, Attendance, Enrollment, Course, Student

# A small, consistent color palette for all charts
COLORS = ["#4361ee", "#4cc9f0", "#f72585", "#f8961e", "#43aa8b", "#7209b7"]


def fig_to_base64(fig):
    """Render a Matplotlib figure to a base64 PNG string for embedding in HTML."""
    buf = BytesIO()
    fig.tight_layout()
    fig.savefig(buf, format="png", dpi=110, transparent=True)
    plt.close(fig)
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "analytics/dashboard.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        # ---------------- Load data into Pandas DataFrames ----------------
        grades_qs = Grade.objects.select_related("enrollment__course", "enrollment__student")

        grade_rows = [
            {
                "course": g.enrollment.course.code,
                "student": g.enrollment.student.full_name,
                "marks": float(g.marks_obtained),
                "letter": g.letter_grade,
            }
            for g in grades_qs
        ]
        grades_df = pd.DataFrame(grade_rows)

        attendance_qs = Attendance.objects.select_related("enrollment__course")
        attendance_rows = [
            {"course": a.enrollment.course.code, "status": a.status, "date": a.date}
            for a in attendance_qs
        ]
        attendance_df = pd.DataFrame(attendance_rows)

        charts = {}
        stats = {}

        if not grades_df.empty:
            # ---- Average marks per course (NumPy + Pandas groupby) ----
            course_avg = grades_df.groupby("course")["marks"].mean().sort_values(ascending=False)
            stats["overall_average"] = round(float(np.mean(grades_df["marks"])), 2)
            stats["overall_std"] = round(float(np.std(grades_df["marks"])), 2)
            stats["top_course"] = course_avg.index[0] if len(course_avg) else "-"
            stats["highest_score"] = round(float(grades_df["marks"].max()), 2)
            stats["lowest_score"] = round(float(grades_df["marks"].min()), 2)

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(course_avg.index, course_avg.values, color=COLORS[0])
            ax.set_title("Average Marks per Course")
            ax.set_ylabel("Average Marks")
            ax.set_xlabel("Course")
            ax.set_ylim(0, 100)
            for i, v in enumerate(course_avg.values):
                ax.text(i, v + 1, f"{v:.1f}", ha="center", fontsize=8)
            charts["avg_marks_chart"] = fig_to_base64(fig)

            # ---- Grade distribution (pie chart) ----
            grade_counts = grades_df["letter"].value_counts().sort_index()
            fig2, ax2 = plt.subplots(figsize=(5, 4))
            ax2.pie(
                grade_counts.values,
                labels=grade_counts.index,
                autopct="%1.0f%%",
                colors=COLORS,
                startangle=90,
            )
            ax2.set_title("Grade Distribution")
            charts["grade_distribution_chart"] = fig_to_base64(fig2)

            # ---- Top 5 students by average marks ----
            top_students = (
                grades_df.groupby("student")["marks"].mean().sort_values(ascending=False).head(5)
            )
            fig3, ax3 = plt.subplots(figsize=(6, 4))
            ax3.barh(top_students.index[::-1], top_students.values[::-1], color=COLORS[2])
            ax3.set_title("Top 5 Students by Average Marks")
            ax3.set_xlabel("Average Marks")
            charts["top_students_chart"] = fig_to_base64(fig3)

            ctx["top_students_table"] = list(
                grades_df.groupby("student")["marks"].mean().sort_values(ascending=False).head(5).items()
            )
        else:
            stats["overall_average"] = 0
            stats["overall_std"] = 0
            stats["top_course"] = "-"
            stats["highest_score"] = 0
            stats["lowest_score"] = 0
            ctx["top_students_table"] = []

        if not attendance_df.empty:
            # ---- Attendance percentage per course ----
            pivot = attendance_df.groupby(["course", "status"]).size().unstack(fill_value=0)
            pivot_pct = pivot.div(pivot.sum(axis=1), axis=0) * 100
            present_pct = pivot_pct.get("present", pd.Series(dtype=float)).sort_values(ascending=False)

            fig4, ax4 = plt.subplots(figsize=(6, 4))
            ax4.bar(present_pct.index, present_pct.values, color=COLORS[4])
            ax4.set_title("Attendance % per Course (Present)")
            ax4.set_ylabel("Present %")
            ax4.set_ylim(0, 100)
            charts["attendance_chart"] = fig_to_base64(fig4)

            stats["overall_attendance_pct"] = round(
                float((attendance_df["status"] == "present").mean() * 100), 2
            )
        else:
            stats["overall_attendance_pct"] = 0

        ctx["charts"] = charts
        ctx["stats"] = stats
        ctx["has_grade_data"] = not grades_df.empty
        ctx["has_attendance_data"] = not attendance_df.empty
        return ctx
