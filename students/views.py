# students/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm


def student_list(request):
    """Show list of all students."""
    students = Student.objects.all().order_by('class_name', 'roll_number')
    context = {"students": students}
    return render(request, "students/student_list.html", context)


def student_detail(request, pk):
    """Show details / professional profile of a single student."""
    student = get_object_or_404(Student, pk=pk)
    context = {"student": student}
    return render(request, "students/student_detail.html", context)


def student_create(request):
    """Create a new student record."""
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()
            # After create, go to detail page for that student
            return redirect("student_detail", pk=student.pk)
    else:
        form = StudentForm()

    context = {
        "form": form,
        "title": "Create Student",
    }
    return render(request, "students/student_form.html", context)


def student_update(request, pk):
    """Update an existing student record."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect("student_detail", pk=student.pk)
    else:
        form = StudentForm(instance=student)

    context = {
        "form": form,
        "title": "Update Student",
        "student": student,
    }
    return render(request, "students/student_form.html", context)


def student_delete(request, pk):
    """Delete a student record (after POST confirm)."""
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")

    context = {"student": student}
    return render(
        request,
        "students/student_confirm_delete.html",
        context,
    )