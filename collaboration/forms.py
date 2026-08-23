
from django import forms

from .models import (
    Discussion,
    Comment
)


class DiscussionForm(forms.ModelForm):

    class Meta:

        model = Discussion

        fields = [

            'title',
            'content',
            'category',
            'image'

        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 6
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

        }


class CommentForm(forms.ModelForm):

    class Meta:

        model = Comment

        fields = [

            'content'

        ]

        widgets = {

            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'placeholder':
                    'Write your reply...'
                }
            )

        }

