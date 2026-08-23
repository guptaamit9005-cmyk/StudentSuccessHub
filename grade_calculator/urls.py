from django.urls import path
from .views import sgpa_calculator

urlpatterns = [

    path(
        '',
        sgpa_calculator,
        name='sgpa_calculator'
    ),

]