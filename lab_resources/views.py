from django.shortcuts import (
    render,
    get_object_or_404
)

from .models import (
    LabSubject,
    LabQuestion
)


def subject_list(request):

    subjects = LabSubject.objects.all().order_by(
        'name'
    )

    return render(
        request,
        'lab_resources/subject_list.html',
        {
            'subjects': subjects
        }
    )


def question_list(request, subject_id):

    subject = get_object_or_404(
        LabSubject,
        id=subject_id
    )

    search_query = request.GET.get(
        'q',
        ''
    )

    questions = subject.questions.all()

    if search_query:

        questions = questions.filter(
            title__icontains=search_query
        )

    questions = questions.order_by(
        '-created_at'
    )

    return render(
        request,
        'lab_resources/question_list.html',
        {
            'subject': subject,
            'questions': questions,
            'search_query': search_query
        }
    )


def question_detail(request, question_id):

    question = get_object_or_404(
        LabQuestion,
        id=question_id
    )

    # Increase view count
    question.views += 1
    question.save()

    return render(
        request,
        'lab_resources/question_detail.html',
        {
            'question': question
        }
    )


def popular_questions(request):

    questions = LabQuestion.objects.order_by(
        '-views'
    )[:10]

    return render(
        request,
        'lab_resources/popular_questions.html',
        {
            'questions': questions
        }
    )