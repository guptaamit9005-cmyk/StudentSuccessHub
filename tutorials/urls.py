from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.tutorial_list,
        name='tutorial_list'
    ),

    path(
        'create/',
        views.create_tutorial,
        name='create_tutorial'
    ),

    path(
        '<slug:slug>/',
        views.tutorial_detail,
        name='tutorial_detail'
    ),

    path(
        '<slug:slug>/update/',
        views.update_tutorial,
        name='update_tutorial'
    ),

    path(
        '<slug:slug>/delete/',
        views.delete_tutorial,
        name='delete_tutorial'
    ),

]