from django.db import models


class Category(models.Model):

    name=models.CharField(max_length=100)

    icon=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):

    LEVELS=(
        ("Beginner","Beginner"),
        ("Intermediate","Intermediate"),
        ("Advanced","Advanced"),
    )

    category=models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    title=models.CharField(max_length=200)

    instructor=models.CharField(max_length=150)

    thumbnail=models.ImageField(
        upload_to="course_thumbnails/"
    )

    youtube_link=models.URLField()

    duration=models.CharField(max_length=50)

    description=models.TextField()

    featured=models.BooleanField(default=False)

    level=models.CharField(
        max_length=20,
        choices=LEVELS
    )

    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title