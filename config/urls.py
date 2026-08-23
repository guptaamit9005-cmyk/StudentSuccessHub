from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def home(request):
    return redirect('login')


urlpatterns = [

    path('', home, name='home'),

    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),

    path('notices/', include('notices.urls')),

    path('resources/', include('resources.urls')),

    path('collaboration/', include('collaboration.urls')),

    path('tracker/', include('academic_tracker.urls')),

    path('grade-calculator/', include('grade_calculator.urls')),

    path('daily-planner/', include('daily_planner.urls')),

    path(
        'coding-contest/',
        include('coding_contest.urls')
    ),

    path(
    'lab-resources/',
    include(
        'lab_resources.urls'
    )
),

path(
    "roadmaps/",
    include("roadmap.urls")
),
path(
    "placement/",
    include("placement_support.urls")
),

path(
    "learning/",
    include("learning_hub.urls")
),
path('students/', include('students.urls')),
  path('tutorials/', include('tutorials.urls')),
]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )