
from django import forms

from .models import Resource


class ResourceForm(forms.ModelForm):

    class Meta:

        model = Resource

        fields = [

            'title',
            'description',
            'category',
            'file',

            'cover_image',
            'tags',
            'external_link'

        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'tags': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':
                    'python, dsa, placement'
                }
            ),

            'external_link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':
                    'https://...'
                }
            ),

        }

