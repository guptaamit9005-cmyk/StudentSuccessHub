from django.urls import path

from .views import (
    contest_list,
    contest_detail,
    problem_detail,
    submit_solution
)

urlpatterns = [

    path(
        '',
        contest_list,
        name='contest_list'
    ),

    path(
        'contest/<int:contest_id>/',
        contest_detail,
        name='contest_detail'
    ),

    path(
        'problem/<int:problem_id>/',
        problem_detail,
        name='problem_detail'
    ),

    path(
        'submit/<int:problem_id>/',
        submit_solution,
        name='submit_solution'
    ),

]