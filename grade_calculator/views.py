from django.shortcuts import render
from .forms import SGPACalculatorForm

def sgpa_calculator(request):
    sgpa = None
    form = SGPACalculatorForm()

    if request.method == "POST":
        form = SGPACalculatorForm(request.POST)
        
        if form.is_valid():
            total_credits = form.cleaned_data['total_credits']
            total_credit_points = form.cleaned_data['total_credit_points']

            if total_credits > 0:
                sgpa = round(total_credit_points / total_credits, 2)
    
    return render(
        request,
        'grade_calculator/sgpa.html',
        {
            'form': form,
            'sgpa': sgpa
        }
    )