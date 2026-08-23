
from django.db import models
from django.conf import settings


class Resource(models.Model):

    CATEGORY_CHOICES = (
        ('python', 'Python'),
        ('java', 'Java'),
        ('dbms', 'DBMS'),
        ('os', 'Operating System'),
        ('cn', 'Computer Networks'),
        ('dsa', 'DSA'),
        ('ai', 'Artificial Intelligence'),
        ('ml', 'Machine Learning'),
        ('placement', 'Placement'),
        ('pyq', 'Previous Year Papers'),
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='python'
    )

    file = models.FileField(
        upload_to='resources/'
    )

    cover_image = models.ImageField(
        upload_to='resource_covers/',
        blank=True,
        null=True
    )

    tags = models.CharField(
        max_length=255,
        blank=True
    )

    external_link = models.URLField(
        blank=True,
        null=True
    )

    view_count = models.PositiveIntegerField(
        default=0
    )

    download_count = models.PositiveIntegerField(
        default=0
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = [
            '-created_at'
        ]

    def __str__(self):

        return self.title

