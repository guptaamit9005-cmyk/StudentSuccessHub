from django.db import models
from django.conf import settings


class Company(models.Model):

    COMPANY_TYPES = (

        ("Product", "Product"),

        ("Service", "Service"),

        ("Startup", "Startup"),

        ("Government", "Government"),

    )

    name = models.CharField(
        max_length=200
    )

    logo = models.ImageField(
        upload_to="companies/",
        blank=True,
        null=True
    )

    company_type = models.CharField(
        max_length=30,
        choices=COMPANY_TYPES
    )

    location = models.CharField(
        max_length=200
    )

    website = models.URLField(
        blank=True
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class JobOpening(models.Model):

    JOB_TYPES = (

        ("Internship", "Internship"),

        ("Full Time", "Full Time"),

        ("Part Time", "Part Time"),

        ("Remote", "Remote"),

    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    title = models.CharField(
        max_length=200
    )

    job_type = models.CharField(
        max_length=30,
        choices=JOB_TYPES
    )

    package = models.CharField(
        max_length=100
    )

    eligibility = models.CharField(
        max_length=200
    )

    skills_required = models.TextField()

    last_date = models.DateField()

    apply_link = models.URLField()

    description = models.TextField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class PlacementApplication(models.Model):

    STATUS = (

        ("Applied", "Applied"),

        ("OA", "Online Assessment"),

        ("Interview", "Interview"),

        ("Selected", "Selected"),

        ("Rejected", "Rejected"),

    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        JobOpening,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default="Applied"
    )

    applied_on = models.DateField(
        auto_now_add=True
    )

    notes = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.job.title}"


class InterviewRound(models.Model):

    ROUND_TYPES = (

        ("OA", "Online Assessment"),

        ("Technical", "Technical"),

        ("HR", "HR"),

        ("Managerial", "Managerial"),

    )

    application = models.ForeignKey(
        PlacementApplication,
        on_delete=models.CASCADE,
        related_name="rounds"
    )

    round_type = models.CharField(
        max_length=30,
        choices=ROUND_TYPES
    )

    interview_date = models.DateField()

    completed = models.BooleanField(
        default=False
    )

    remarks = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.round_type


class Skill(models.Model):

    name = models.CharField(
        max_length=100
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name