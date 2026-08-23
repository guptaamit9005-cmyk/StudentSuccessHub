from django.shortcuts import render

from .models import (
    Company,
    JobOpening,
    PlacementApplication,
    InterviewRound
)

def dashboard(request):

    search = request.GET.get("search")

    companies = Company.objects.all()

    if search:

        companies = companies.filter(
            name__icontains=search
        )

    context = {

        "companies": companies,

        "search": search,

        "total_companies": Company.objects.count(),

        "total_jobs": JobOpening.objects.count(),

        "total_applications": PlacementApplication.objects.count(),

        "total_interviews": InterviewRound.objects.count(),

    }

    return render(

        request,

        "placement_support/dashboard.html",

        context

    )