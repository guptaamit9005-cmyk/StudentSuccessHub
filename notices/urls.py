from django.urls import path

from .views import (
    notice_list,
    notice_detail,
    create_notice,
    edit_notice,
    delete_notice
)

urlpatterns = [

    path(
        '',
        notice_list,
        name='notice_list'
    ),

    path(
        'create/',
        create_notice,
        name='create_notice'
    ),

    path(
        'edit/<int:pk>/',
        edit_notice,
        name='edit_notice'
    ),

    path(
        'delete/<int:pk>/',
        delete_notice,
        name='delete_notice'
    ),

    path(
        '<int:pk>/',
        notice_detail,
        name='notice_detail'
    ),
]