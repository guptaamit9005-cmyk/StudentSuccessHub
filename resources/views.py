
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Resource
from .forms import ResourceForm


@login_required
def resource_list(request):

    resources = Resource.objects.all()

    search = request.GET.get('search')

    if search:

        resources = resources.filter(
            title__icontains=search
        )

    return render(
        request,
        'resources/resource_list.html',
        {
            'resources': resources
        }
    )


@login_required
def create_resource(request):

    if request.user.role != 'cr':

        return HttpResponseForbidden(
            "Only CR can upload resources."
        )

    if request.method == 'POST':

        form = ResourceForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            resource = form.save(
                commit=False
            )

            resource.uploaded_by = request.user

            resource.save()

            return redirect(
                'resource_list'
            )

    else:

        form = ResourceForm()

    return render(
        request,
        'resources/create_resource.html',
        {
            'form': form
        }
    )

