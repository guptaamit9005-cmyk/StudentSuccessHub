from django.urls import path
from .views import syllabus_dashboard, subject_detail, mark_topic_complete

urlpatterns = [
    path(
        '',
        syllabus_dashboard,
        name='syllabus_dashboard'
    ),
    path(
        'subject/<int:subject_id>/',
        subject_detail,
        name='subject_detail'
    ),
    path(
        'topic/<int:topic_id>/toggle/',
        mark_topic_complete,
        name='mark_topic_complete'
    ),
]