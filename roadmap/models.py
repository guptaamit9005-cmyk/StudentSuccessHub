from django.db import models
from django.conf import settings


class RoadmapCategory(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    icon = models.CharField(
        max_length=50,
        default="📚"
    )

    color = models.CharField(
        max_length=30,
        default="#6366F1"
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Roadmap Categories"

    def __str__(self):
        return self.name


class Roadmap(models.Model):

    DIFFICULTY = (

        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),

    )

    VISIBILITY = (

        ('Public', 'Public'),
        ('Private', 'Private'),

    )

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="roadmaps"
    )

    category = models.ForeignKey(
        RoadmapCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    title = models.CharField(
        max_length=250
    )

    subtitle = models.CharField(
        max_length=300,
        blank=True
    )

    description = models.TextField()

    thumbnail = models.ImageField(
        upload_to="roadmaps/",
        blank=True,
        null=True
    )

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY,
        default="Beginner"
    )

    visibility = models.CharField(
        max_length=20,
        choices=VISIBILITY,
        default="Public"
    )

    estimated_time = models.CharField(
        max_length=100,
        default="3 Months"
    )

    progress = models.PositiveIntegerField(
        default=0
    )

    featured = models.BooleanField(
        default=False
    )

    total_views = models.PositiveIntegerField(
        default=0
    )

    total_likes = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class RoadmapStep(models.Model):

    roadmap = models.ForeignKey(
        Roadmap,
        on_delete=models.CASCADE,
        related_name="steps"
    )

    title = models.CharField(
        max_length=250
    )

    description = models.TextField(
        blank=True
    )

    step_number = models.PositiveIntegerField()

    estimated_days = models.PositiveIntegerField(
        default=7
    )

    completed = models.BooleanField(
        default=False
    )

    resource_link = models.URLField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"{self.step_number}. {self.title}"