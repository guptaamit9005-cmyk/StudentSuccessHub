
from django import forms
from .models import Notice


class NoticeForm(forms.ModelForm):

    class Meta:

        model = Notice

        fields = [
            'title',
            'description',
            'category',
            'image',
            'pdf_file',
            'external_link',
            'deadline',
            'target_audience',
            'tags',
            'important',
            'pinned',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter notice title'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 5,
                    'placeholder': 'Write notice details'
                }
            ),

            'category': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'external_link': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Google Meet / Zoom / Drive / YouTube Link'
                }
            ),

            'deadline': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),

            'target_audience': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'tags': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Python, Java, Placement, DSA'
                }
            ),

            'important': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),

            'pinned': forms.CheckboxInput(
                attrs={
                    'class': 'form-check-input'
                }
            ),
        }
