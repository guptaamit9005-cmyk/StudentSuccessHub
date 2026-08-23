from django import forms


class SGPACalculatorForm(forms.Form):

    total_credits = forms.FloatField(
        label="Total Credits",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Example: 22'
            }
        )
    )

    total_credit_points = forms.FloatField(
        label="Total Credit Points",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Example: 198'
            }
        )
    )