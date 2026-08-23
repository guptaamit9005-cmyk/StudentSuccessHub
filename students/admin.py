from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'roll_number', 'class_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'roll_number', 'class_name', 'email')
    list_filter = ('class_name', 'section')