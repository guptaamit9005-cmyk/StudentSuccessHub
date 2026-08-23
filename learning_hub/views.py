from django.shortcuts import render

from .models import *


def home(request):

    categories=Category.objects.all()

    featured=Course.objects.filter(featured=True)

    latest=Course.objects.order_by("-created")[:8]

    context={

        "categories":categories,

        "featured":featured,

        "latest":latest,

    }

    return render(
        request,
        "learning_hub/home.html",
        context
    )