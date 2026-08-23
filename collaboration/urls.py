
from django.urls import path

from .views import (

    discussion_list,
    create_discussion,
    discussion_detail,
    like_discussion,

    edit_discussion,
    delete_discussion,

)

urlpatterns = [

    path(
        '',
        discussion_list,
        name='discussion_list'
    ),

    path(
        'create/',
        create_discussion,
        name='create_discussion'
    ),

    path(
        '<int:pk>/',
        discussion_detail,
        name='discussion_detail'
    ),

    path(
        'like/<int:pk>/',
        like_discussion,
        name='like_discussion'
    ),

    path(
        'edit/<int:pk>/',
        edit_discussion,
        name='edit_discussion'
    ),

    path(
        'delete/<int:pk>/',
        delete_discussion,
        name='delete_discussion'
    ),

]

