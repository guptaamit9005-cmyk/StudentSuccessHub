from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import (
    Roadmap,
    RoadmapStep
)

from .forms import (
    RoadmapForm
)


@login_required
def roadmap_list(request):

    roadmaps = Roadmap.objects.all()

    search = request.GET.get("search")

    if search:

        roadmaps = roadmaps.filter(
            title__icontains=search
        )

    total_roadmaps = roadmaps.count()

    context = {

        "roadmaps": roadmaps,

        "total_roadmaps": total_roadmaps,

        "search": search

    }

    return render(
        request,
        "roadmap/roadmap_list.html",
        context
    )


@login_required
def create_roadmap(request):

    if request.method == "POST":

        form = RoadmapForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            roadmap = form.save(
                commit=False
            )

            roadmap.creator = request.user

            roadmap.save()

            return redirect(
                "roadmap_list"
            )

    else:

        form = RoadmapForm()

    return render(

        request,

        "roadmap/create_roadmap.html",

        {

            "form": form

        }

    )


@login_required
def roadmap_detail(request, roadmap_id):

    roadmap = get_object_or_404(

        Roadmap,

        id=roadmap_id

    )

    steps = RoadmapStep.objects.filter(

        roadmap=roadmap

    )

    completed = steps.filter(

        completed=True

    ).count()

    total = steps.count()

    progress = 0

    if total > 0:

        progress = int(

            completed / total * 100

        )

    return render(

        request,

        "roadmap/roadmap_detail.html",

        {

            "roadmap": roadmap,

            "steps": steps,

            "progress": progress

        }

    )


@login_required
def delete_roadmap(request, roadmap_id):

    roadmap = get_object_or_404(

        Roadmap,

        id=roadmap_id,

        creator=request.user

    )

    roadmap.delete()

    return redirect(

        "roadmap_list"

    )