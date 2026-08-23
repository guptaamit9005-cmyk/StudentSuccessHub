from django import forms

from .models import Submission


class SubmissionForm(forms.ModelForm):

    class Meta:

        model = Submission

        fields = [
            'github_link'
        ]

        widgets = {

            'github_link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':
                    'https://github.com/username/repo'
                }
            )

        }