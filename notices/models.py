
from django.db import models
from django.conf import settings


class Notice(models.Model):

    CATEGORY_CHOICES = (
        ('exam', 'Exam'),
        ('assignment', 'Assignment'),
        ('placement', 'Placement'),
        ('event', 'Event'),
        ('workshop', 'Workshop'),
        ('hackathon', 'Hackathon'),
        ('internship', 'Internship'),
        ('urgent', 'Urgent'),
    )

    AUDIENCE_CHOICES = (
        ('all', 'All Students'),
        ('bca', 'Only BCA'),
        ('first_year', 'Only 1st Year'),
        ('second_year', 'Only 2nd Year'),
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='event'
    )

    image = models.ImageField(
        upload_to='notice_images/',
        blank=True,
        null=True
    )

    pdf_file = models.FileField(
        upload_to='notice_pdfs/',
        blank=True,
        null=True
    )

    external_link = models.URLField(
        blank=True,
        null=True
    )

    deadline = models.DateField(
        blank=True,
        null=True
    )

    target_audience = models.CharField(
        max_length=50,
        choices=AUDIENCE_CHOICES,
        default='all'
    )

    tags = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    pinned = models.BooleanField(default=False)

    important = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            '-pinned',
            '-important',
            '-created_at'
        ]

    def __str__(self):
        return self.title
