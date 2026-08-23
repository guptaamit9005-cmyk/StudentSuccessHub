from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'roll_number', 'email',
            'class_name', 'section', 'date_of_birth',
            'phone', 'address',
            'guardian_name', 'guardian_phone',
        ]