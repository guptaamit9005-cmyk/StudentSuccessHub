from django.shortcuts import render, get_object_or_404, redirect

from .models import (
    Subject,
    Topic,
    TopicProgress,
    WeeklyGoal
)


def syllabus_dashboard(request):
    subjects = Subject.objects.all()

    total_subjects = subjects.count()
    total_topics = Topic.objects.count()

    completed_topics = 0
    completed_goals = 0

    if request.user.is_authenticated:
        completed_topics = TopicProgress.objects.filter(
            user=request.user,
            completed=True
        ).count()

        completed_goals = WeeklyGoal.objects.filter(
            user=request.user,
            completed=True
        ).count()

    return render(
        request,
        'academic_tracker/dashboard.html',
        {
            'subjects': subjects,
            'total_subjects': total_subjects,
            'total_topics': total_topics,
            'completed_topics': completed_topics,
            'completed_goals': completed_goals,
        }
    )


def subject_detail(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    units = subject.units.all()

    total_topics = Topic.objects.filter(
        unit__subject=subject
    ).count()

    completed_topic_ids = []
    progress = 0

    if request.user.is_authenticated:
        completed_progress = TopicProgress.objects.filter(
            user=request.user,
            topic__unit__subject=subject,
            completed=True
        )

        completed_topics_count = completed_progress.count()

        completed_topic_ids = list(
            completed_progress.values_list('topic_id', flat=True)
        )

        if total_topics > 0:
            progress = int(
                (completed_topics_count / total_topics) * 100
            )

    return render(
        request,
        'academic_tracker/subject_detail.html',
        {
            'subject': subject,
            'units': units,
            'progress': progress,
            'completed_topic_ids': completed_topic_ids,
        }
    )


def mark_topic_complete(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    progress, created = TopicProgress.objects.get_or_create(
        user=request.user,
        topic=topic
    )

    progress.completed = not progress.completed
    progress.save()

    return redirect(
        'subject_detail',
        subject_id=topic.unit.subject.id
    )