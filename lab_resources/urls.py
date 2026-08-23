from django.urls import path

from .views import (
    subject_list,
    question_list,
    question_detail,
    popular_questions
)

urlpatterns = [

    path(
        '',
        subject_list,
        name='lab_subjects'
    ),

    path(
        'subject/<int:subject_id>/',
        question_list,
        name='lab_questions'
    ),

    path(
        'question/<int:question_id>/',
        question_detail,
        name='question_detail'
    ),

    path(
        'popular/',
        popular_questions,
        name='popular_questions'
    ),

]