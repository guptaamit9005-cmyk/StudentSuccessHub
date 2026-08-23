from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


# =========================================================
# HOME
# =========================================================

def home(request):
    """
    Redirect the root URL to the login page.
    """
    return redirect("login")


# =========================================================
# URL PATTERNS
# =========================================================

urlpatterns = [

    # -----------------------------------------------------
    # Home
    # -----------------------------------------------------

    path(
        "",
        home,
        name="home"
    ),

    # -----------------------------------------------------
    # Django Admin
    # -----------------------------------------------------

    path(
        "admin/",
        admin.site.urls
    ),

    # -----------------------------------------------------
    # Accounts
    # Login / Register / Logout / Profile
    # -----------------------------------------------------

    path(
        "",
        include("accounts.urls")
    ),

    # -----------------------------------------------------
    # Notices
    # -----------------------------------------------------

    path(
        "notices/",
        include("notices.urls")
    ),

    # -----------------------------------------------------
    # Resources
    # -----------------------------------------------------

    path(
        "resources/",
        include("resources.urls")
    ),

    # -----------------------------------------------------
    # Collaboration
    # -----------------------------------------------------

    path(
        "collaboration/",
        include("collaboration.urls")
    ),

    # -----------------------------------------------------
    # Academic / Syllabus Tracker
    # -----------------------------------------------------

    path(
        "tracker/",
        include("academic_tracker.urls")
    ),

    # -----------------------------------------------------
    # Grade Calculator
    # -----------------------------------------------------

    path(
        "grade-calculator/",
        include("grade_calculator.urls")
    ),

    # -----------------------------------------------------
    # Daily Planner
    # -----------------------------------------------------

    path(
        "daily-planner/",
        include("daily_planner.urls")
    ),

    # -----------------------------------------------------
    # Coding Contest
    # -----------------------------------------------------

    path(
        "coding-contest/",
        include("coding_contest.urls")
    ),

    # -----------------------------------------------------
    # Lab Resources
    # -----------------------------------------------------

    path(
        "lab-resources/",
        include("lab_resources.urls")
    ),

    # -----------------------------------------------------
    # Roadmaps
    # -----------------------------------------------------

    path(
        "roadmaps/",
        include("roadmap.urls")
    ),

    # -----------------------------------------------------
    # Placement Support
    # -----------------------------------------------------

    path(
        "placement/",
        include("placement_support.urls")
    ),

    # -----------------------------------------------------
    # Learning Hub
    # -----------------------------------------------------

    path(
        "learning/",
        include("learning_hub.urls")
    ),

    # -----------------------------------------------------
    # Students
    # -----------------------------------------------------

    path(
        "students/",
        include("students.urls")
    ),

    # -----------------------------------------------------
    # Tutorials & Articles
    # -----------------------------------------------------

    path(
        "tutorials/",
        include("tutorials.urls")
    ),
]


# =========================================================
# DEVELOPMENT MEDIA FILES
# =========================================================
#
# Django development server will serve uploaded media
# files when DEBUG=True.
#
# In production (Render), DEBUG will be False and this
# block will not run. Production media/PDF storage will
# be handled separately.
# =========================================================

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )