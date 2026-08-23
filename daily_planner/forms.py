from django import forms
from .models import StudyTask


class StudyTaskForm(forms.ModelForm):
    class Meta:
        model = StudyTask
        fields = [
            'title',
            'description',
            'priority'
        ]
        
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter task title'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 4,
                    'placeholder': 'Enter task description'
                }
            ),
            'priority': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }
        
        labels = {
            'title': 'Task Title',
            'description': 'Description',
            'priority': 'Priority'
        }