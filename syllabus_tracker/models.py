from django.db import models
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(
        max_length=200
    )

    code = models.CharField(
        max_length=20
    )

    semester = models.IntegerField()

    description = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Unit(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name='units'
    )

    title = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.title


class Topic(models.Model):
    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name='topics'
    )

    title = models.CharField(
        max_length=300
    )

    def __str__(self):
        return self.title


class TopicProgress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE
    )

    completed = models.BooleanField(
        default=False
    )

    completed_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        unique_together = (
            'user',
            'topic'
        )

    def __str__(self):
        return f"{self.user.username} - {self.topic.title}"


class StudyStreak(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    current_streak = models.PositiveIntegerField(
        default=0
    )

    longest_streak = models.PositiveIntegerField(
        default=0
    )

    last_study_date = models.DateField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username


class WeeklyGoal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class StudySession(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    study_hours = models.FloatField()

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.subject.name}"


class RevisionTask(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    revision_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class Achievement(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    badge_name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    earned_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.badge_name
