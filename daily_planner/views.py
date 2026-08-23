from datetime import timedelta
from django.shortcuts import (
    render, redirect, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import StudyTask
from .forms import StudyTaskForm


@login_required
def planner_home(request):
    tasks = StudyTask.objects.filter(
        user=request.user
    ).order_by('-created_at')

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(completed=True).count()
    pending_tasks = tasks.filter(completed=False).count()

    progress_percentage = 0
    if total_tasks > 0:
        progress_percentage = int(
            (completed_tasks / total_tasks) * 100
        )

    # Additional stats
    today_tasks = tasks.filter(
        created_at__date=timezone.now().date()
    ).count()

    high_priority_tasks = tasks.filter(
        priority='high'
    ).count()

    week_start = timezone.now() - timedelta(days=7)
    weekly_tasks = tasks.filter(
        created_at__gte=week_start
    ).count()

    if request.method == 'POST':
        form = StudyTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('planner_home')
    else:
        form = StudyTaskForm()

    return render(
        request,
        'daily_planner/planner_home.html',
        {
            'form': form,
            'tasks': tasks,
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks,
            'progress_percentage': progress_percentage,
            'today_tasks': today_tasks,
            'high_priority_tasks': high_priority_tasks,
            'weekly_tasks': weekly_tasks,
        }
    )


@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(
        StudyTask,
        id=task_id,
        user=request.user
    )
    task.completed = not task.completed
    task.save()
    return redirect('planner_home')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(
        StudyTask,
        id=task_id,
        user=request.user
    )
    task.delete()
    return redirect('planner_home')