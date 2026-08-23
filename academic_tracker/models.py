from django.db import models
from django.conf import settings


class Subject(models.Model):

    name = models.CharField(max_length=200)

    code = models.CharField(max_length=20)

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

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Topic(models.Model):

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name='topics'
    )

    title = models.CharField(max_length=300)

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

    class Meta:
        unique_together = (
            'user',
            'topic'
        )

    def __str__(self):
        return f"{self.user.username} - {self.topic.title}"
