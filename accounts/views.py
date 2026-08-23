
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .forms import ProfileUpdateForm

from notices.models import Notice
from resources.models import Resource
from collaboration.models import Discussion


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect('dashboard')

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


@login_required
def dashboard_view(request):

    notice_count = Notice.objects.count()

    resource_count = Resource.objects.count()

    discussion_count = Discussion.objects.count()

    return render(
        request,
        'accounts/dashboard.html',
        {
            'notice_count': notice_count,
            'resource_count': resource_count,
            'discussion_count': discussion_count,
        }
    )


@login_required
def profile_view(request):

    return render(
        request,
        'accounts/profile.html'
    )


@login_required
def edit_profile_view(request):

    if request.method == 'POST':

        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user
        )

        if form.is_valid():

            form.save()

            return redirect(
                'profile'
            )

    else:

        form = ProfileUpdateForm(
            instance=request.user
        )

    return render(
        request,
        'accounts/edit_profile.html',
        {
            'form': form
        }
    )

