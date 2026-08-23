from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Tutorial, Category
from .forms import TutorialForm


def tutorial_list(request):

    tutorials = Tutorial.objects.all()

    search = request.GET.get("search")

    category = request.GET.get("category")

    if search:
        tutorials = tutorials.filter(title__icontains=search)

    if category:
        tutorials = tutorials.filter(category__slug=category)

    paginator = Paginator(tutorials, 6)

    page = request.GET.get("page")

    tutorials = paginator.get_page(page)

    categories = Category.objects.all()

    return render(
        request,
        "tutorials/tutorial_list.html",
        {
            "tutorials": tutorials,
            "categories": categories,
        },
    )


def tutorial_detail(request, slug):

    tutorial = get_object_or_404(
        Tutorial,
        slug=slug
    )

    tutorial.views += 1

    tutorial.save()

    return render(
        request,
        "tutorials/tutorial_detail.html",
        {
            "tutorial": tutorial
        },
    )


@login_required
def create_tutorial(request):

    if request.method == "POST":

        form = TutorialForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            tutorial = form.save(commit=False)

            tutorial.author = request.user

            tutorial.save()

            return redirect(tutorial)

    else:

        form = TutorialForm()

    return render(
        request,
        "tutorials/create_tutorial.html",
        {
            "form": form
        },
    )


@login_required
def update_tutorial(request, slug):

    tutorial = get_object_or_404(
        Tutorial,
        slug=slug
    )

    form = TutorialForm(
        request.POST or None,
        request.FILES or None,
        instance=tutorial
    )

    if form.is_valid():

        form.save()

        return redirect(tutorial)

    return render(
        request,
        "tutorials/update_tutorial.html",
        {
            "form": form,
            "tutorial": tutorial,
        },
    )


@login_required
def delete_tutorial(request, slug):

    tutorial = get_object_or_404(
        Tutorial,
        slug=slug
    )

    if request.method == "POST":

        tutorial.delete()

        return redirect("tutorial_list")

    return render(
        request,
        "tutorials/delete_tutorial.html",
        {
            "tutorial": tutorial
        },
    )