from django.db import models
from django.conf import settings


class Contest(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title


class Problem(models.Model):

    DIFFICULTY_CHOICES = (

        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),

    )

    contest = models.ForeignKey(
        Contest,
        on_delete=models.CASCADE,
        related_name='problems'
    )

    title = models.CharField(
        max_length=200
    )

    statement = models.TextField()

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES,
        default='Easy'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title


class Submission(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    problem = models.ForeignKey(
        Problem,
        on_delete=models.CASCADE,
        related_name='submissions'
    )

    github_link = models.URLField()

    submitted_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return (
            f"{self.user.username} - "
            f"{self.problem.title}"
        )