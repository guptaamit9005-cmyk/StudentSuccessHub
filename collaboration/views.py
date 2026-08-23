
from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import (
    Discussion,
    Comment
)

from .forms import (
    DiscussionForm,
    CommentForm
)


@login_required
def discussion_list(request):

    discussions = Discussion.objects.all()

    search = request.GET.get('search')

    category = request.GET.get(
        'category'
    )

    if search:

        discussions = discussions.filter(
            title__icontains=search
        )

    if category:

        discussions = discussions.filter(
            category=category
        )

    trending_discussions = Discussion.objects.all().order_by(
        '-created_at'
    )[:5]

    return render(
        request,
        'collaboration/discussion_list.html',
        {
            'discussions': discussions,
            'trending_discussions': trending_discussions,
        }
    )


@login_required
def create_discussion(request):

    if request.method == 'POST':

        form = DiscussionForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            discussion = form.save(
                commit=False
            )

            discussion.author = request.user

            discussion.save()

            return redirect(
                'discussion_list'
            )

    else:

        form = DiscussionForm()

    return render(
        request,
        'collaboration/create_discussion.html',
        {
            'form': form
        }
    )


@login_required
def discussion_detail(request, pk):

    discussion = get_object_or_404(
        Discussion,
        pk=pk
    )

    if request.method == 'POST':

        comment_form = CommentForm(
            request.POST
        )

        if comment_form.is_valid():

            comment = comment_form.save(
                commit=False
            )

            comment.author = request.user

            comment.discussion = discussion

            comment.save()

            return redirect(
                'discussion_detail',
                pk=pk
            )

    else:

        comment_form = CommentForm()

    return render(
        request,
        'collaboration/discussion_detail.html',
        {
            'discussion': discussion,
            'comment_form': comment_form
        }
    )


@login_required
def like_discussion(request, pk):

    discussion = get_object_or_404(
        Discussion,
        pk=pk
    )

    if request.user in discussion.likes.all():

        discussion.likes.remove(
            request.user
        )

    else:

        discussion.likes.add(
            request.user
        )

    return redirect(
        'discussion_detail',
        pk=pk
    )


@login_required
def edit_discussion(request, pk):

    discussion = get_object_or_404(
        Discussion,
        pk=pk
    )

    if discussion.author != request.user:

        return redirect(
            'discussion_detail',
            pk=pk
        )

    if request.method == 'POST':

        form = DiscussionForm(
            request.POST,
            request.FILES,
            instance=discussion
        )

        if form.is_valid():

            form.save()

            return redirect(
                'discussion_detail',
                pk=pk
            )

    else:

        form = DiscussionForm(
            instance=discussion
        )

    return render(
        request,
        'collaboration/create_discussion.html',
        {
            'form': form
        }
    )


@login_required
def delete_discussion(request, pk):

    discussion = get_object_or_404(
        Discussion,
        pk=pk
    )

    if discussion.author == request.user:

        discussion.delete()

    return redirect(
        'discussion_list'
    )



