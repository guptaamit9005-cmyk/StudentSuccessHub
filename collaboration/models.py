
from django.db import models
from django.conf import settings


class Discussion(models.Model):

    CATEGORY_CHOICES = (

        ('general', 'General'),
        ('programming', 'Programming'),
        ('placement', 'Placement'),
        ('hackathon', 'Hackathon'),
        ('project', 'Project'),
        ('exam', 'Exam'),

    )

    title = models.CharField(
        max_length=255
    )

    content = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to='discussion_images/',
        blank=True,
        null=True
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_discussions',
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def total_likes(self):

        return self.likes.count()

    def __str__(self):

        return self.title


class Comment(models.Model):

    discussion = models.ForeignKey(
        Discussion,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.author.username


