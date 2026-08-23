from django.db import models


class LabSubject(models.Model):

    name = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name


class LabQuestion(models.Model):

    DIFFICULTY_CHOICES = (

        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),

    )

    subject = models.ForeignKey(
        LabSubject,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    title = models.CharField(
        max_length=300
    )

    question = models.TextField()

    solution = models.TextField(
        help_text="Add the solution code here"
    )

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default='Easy'
    )

    viva_questions = models.TextField(
        blank=True,
        null=True,
        help_text="Add viva questions here"
    )

    pdf_notes = models.FileField(
        upload_to='lab_notes/',
        blank=True,
        null=True
    )

    views = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):

        return self.title