from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Contest, Problem, Submission
from .forms import SubmissionForm


def contest_list(request):
    contests = Contest.objects.all().order_by('-start_date')
    
    return render(
        request,
        'coding_contest/contest_list.html',
        {'contests': contests}
    )


def contest_detail(request, contest_id):
    contest = get_object_or_404(Contest, id=contest_id)
    problems = contest.problems.all()

    # Count unique participants who made at least one submission
    participants_count = Submission.objects.filter(
        problem__contest=contest
    ).values('user').distinct().count()

    return render(
        request,
        'coding_contest/contest_detail.html',
        {
            'contest': contest,
            'problems': problems,
            'participants_count': participants_count,
        }
    )


def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)

    submissions = []
    if request.user.is_authenticated:
        submissions = Submission.objects.filter(
            user=request.user,
            problem=problem
        ).order_by('-submitted_at')

    return render(
        request,
        'coding_contest/problem_detail.html',
        {
            'problem': problem,
            'submissions': submissions,
        }
    )


@login_required
def submit_solution(request, problem_id):
    problem = get_object_or_404(Problem, id=problem_id)

    if request.method == 'POST':
        form = SubmissionForm(request.POST)
        
        if form.is_valid():
            submission = form.save(commit=False)
            submission.user = request.user
            submission.problem = problem
            submission.save()

            messages.success(
                request, 
                "Your solution has been submitted successfully!"
            )
            return redirect('problem_detail', problem_id=problem.id)
    else:
        form = SubmissionForm()

    return render(
        request,
        'coding_contest/submit_solution.html',
        {
            'problem': problem,
            'form': form,
        }
    )