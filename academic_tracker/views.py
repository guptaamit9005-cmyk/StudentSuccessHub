from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import (
    Subject,
    Unit,
    Topic,
    TopicProgress
)


def syllabus_dashboard(request):
    subjects = Subject.objects.all()

    return render(
        request,
        'academic_tracker/dashboard.html',
        {
            'subjects': subjects
        }
    )


def subject_detail(request, subject_id):

    subject = get_object_or_404(
        Subject,
        id=subject_id
    )

    units = subject.units.all()

    total_topics = Topic.objects.filter(
        unit__subject=subject
    ).count()

    completed_topic_ids = []
    progress_percentage = 0

    if request.user.is_authenticated:

        completed_progress = TopicProgress.objects.filter(
            user=request.user,
            topic__unit__subject=subject,
            completed=True
        )

        completed_topics_count = completed_progress.count()

        completed_topic_ids = list(
            completed_progress.values_list(
                'topic_id',
                flat=True
            )
        )

        if total_topics > 0:
            progress_percentage = int(
                (completed_topics_count / total_topics) * 100
            )

    return render(
        request,
        'academic_tracker/subject_detail.html',
        {
            'subject': subject,
            'units': units,
            'progress': progress_percentage,
            'completed_topic_ids': completed_topic_ids,
        }
    )


@login_required
def mark_topic_complete(request, topic_id):

    topic = get_object_or_404(
        Topic,
        id=topic_id
    )

    topic_progress, created = TopicProgress.objects.get_or_create(
        user=request.user,
        topic=topic
    )

    topic_progress.completed = not topic_progress.completed
    topic_progress.save()

    return redirect(
        'subject_detail',
        subject_id=topic.unit.subject.id
    )
