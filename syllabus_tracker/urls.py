from django.urls import path

from .views import (
    syllabus_dashboard,
    subject_detail,
    mark_topic_complete,
    revision_tasks,
    complete_revision_task
)

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

    path(
        'revision/',
        revision_tasks,
        name='revision_tasks'
    ),

    path(
        'revision/<int:task_id>/complete/',
        complete_revision_task,
        name='complete_revision_task'
    ),

]