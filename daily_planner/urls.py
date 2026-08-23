from django.urls import path

from .views import (
    planner_home,
    toggle_task,
    delete_task
)

urlpatterns = [

    path(
        '',
        planner_home,
        name='planner_home'
    ),

    path(
        'toggle/<int:task_id>/',
        toggle_task,
        name='toggle_task'
    ),

    path(
        'delete/<int:task_id>/',
        delete_task,
        name='delete_task'
    ),

]