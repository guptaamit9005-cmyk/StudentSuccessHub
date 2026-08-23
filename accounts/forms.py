
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField(
        required=True
    )

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'bio',
            'profile_picture',
            'password1',
            'password2'
        ]

        widgets = {

            'bio': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Tell us about yourself'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter your email'
                }
            ),

            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Choose a username'
                }
            ),

        }


class ProfileUpdateForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            'email',
            'bio',
            'profile_picture'
        ]

        widgets = {

            'bio': forms.Textarea(
                attrs={
                    'rows': 4
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Update your email'
                }
            ),

        }

