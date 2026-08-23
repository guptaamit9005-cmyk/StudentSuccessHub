from django.db import models

class Student(models.Model):
    # Basic identity
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)

    # Class & academic info
    class_name = models.CharField(max_length=50)      # e.g. "Class 10-A"
    section = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    # Contact details
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    # Extra info
    guardian_name = models.CharField(max_length=100, blank=True)
    guardian_phone = models.CharField(max_length=15, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_number})"