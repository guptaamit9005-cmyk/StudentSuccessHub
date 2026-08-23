from django import forms

from .models import (
    Roadmap,
    RoadmapStep
)


class RoadmapForm(forms.ModelForm):

    class Meta:

        model = Roadmap

        fields = [

            'category',

            'title',

            'subtitle',

            'description',

            'thumbnail',

            'difficulty',

            'visibility',

            'estimated_time',

        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Roadmap Title'
                }
            ),

            'subtitle': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Short Subtitle'
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

            'difficulty': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'visibility': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'estimated_time': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Example: 6 Months'
                }
            ),

        }


class RoadmapStepForm(forms.ModelForm):

    class Meta:

        model = RoadmapStep

        fields = [

            'title',

            'description',

            'estimated_days',

            'resource_link',

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
                    'rows': 4
                }
            ),

            'estimated_days': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'resource_link': forms.URLInput(
                attrs={
                    'class': 'form-control'
                }
            )

        }