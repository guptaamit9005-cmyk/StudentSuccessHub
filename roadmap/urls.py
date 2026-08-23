from django.urls import path

from .views import (

    roadmap_list,

    create_roadmap,

    roadmap_detail,

    delete_roadmap,

)

urlpatterns = [

    path(

        "",

        roadmap_list,

        name="roadmap_list"

    ),

    path(

        "create/",

        create_roadmap,

        name="create_roadmap"

    ),

    path(

        "<int:roadmap_id>/",

        roadmap_detail,

        name="roadmap_detail"

    ),

    path(

        "delete/<int:roadmap_id>/",

        delete_roadmap,

        name="delete_roadmap"

    ),

]
