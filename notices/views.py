
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Notice
from .forms import NoticeForm


@login_required
def notice_list(request):

    notices = Notice.objects.all()

    search = request.GET.get('search')
    category = request.GET.get('category')

    if search:
        notices = notices.filter(
            title__icontains=search
        )

    if category:
        notices = notices.filter(
            category=category
        )

    return render(
        request,
        'notices/notice_list.html',
        {
            'notices': notices
        }
    )


@login_required
def notice_detail(request, pk):

    notice = get_object_or_404(
        Notice,
        pk=pk
    )

    return render(
        request,
        'notices/notice_detail.html',
        {
            'notice': notice
        }
    )


@login_required
def create_notice(request):

    if request.user.role != 'cr':

        return HttpResponseForbidden(
            "Only CR can create notices."
        )

    if request.method == 'POST':

        form = NoticeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            notice = form.save(
                commit=False
            )

            notice.created_by = request.user

            notice.save()

            return redirect(
                'notice_list'
            )

        else:

            print("FORM ERROR")
            print(form.errors)

    else:

        form = NoticeForm()

    return render(
        request,
        'notices/create_notice.html',
        {
            'form': form
        }
    )


@login_required
def edit_notice(request, pk):

    notice = get_object_or_404(
        Notice,
        pk=pk
    )

    if request.user.role != 'cr':

        return HttpResponseForbidden(
            "Only CR can edit notices."
        )

    if request.method == 'POST':

        form = NoticeForm(
            request.POST,
            request.FILES,
            instance=notice
        )

        if form.is_valid():

            form.save()

            return redirect(
                'notice_detail',
                pk=notice.pk
            )

        else:

            print(form.errors)

    else:

        form = NoticeForm(
            instance=notice
        )

    return render(
        request,
        'notices/create_notice.html',
        {
            'form': form
        }
    )


@login_required
def delete_notice(request, pk):

    notice = get_object_or_404(
        Notice,
        pk=pk
    )

    if request.user.role != 'cr':

        return HttpResponseForbidden(
            "Only CR can delete notices."
        )

    notice.delete()

    return redirect(
        'notice_list'
    )


