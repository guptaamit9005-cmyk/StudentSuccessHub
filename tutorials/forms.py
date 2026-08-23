from django import forms
from .models import Tutorial


class TutorialForm(forms.ModelForm):

    class Meta:
        model = Tutorial

        fields = [
            'title',
            'slug',
            'category',
            'thumbnail',
            'short_description',
            'content',
            'youtube_link',
            'level',
            'reading_time',
            'featured',
        ]

        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'slug': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'category': forms.Select(attrs={
                'class': 'form-select'
            }),

            'short_description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 12
            }),

            'youtube_link': forms.URLInput(attrs={
                'class': 'form-control'
            }),

            'level': forms.Select(attrs={
                'class': 'form-select'
            }),

            'reading_time': forms.NumberInput(attrs={
                'class': 'form-control'
            }),

            'featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }