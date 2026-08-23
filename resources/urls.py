
from django.urls import path

from .views import (
    resource_list,
    create_resource,
)

urlpatterns = [

    path(
        '',
        resource_list,
        name='resource_list'
    ),

    path(
        'create/',
        create_resource,
        name='create_resource'
    ),

]

