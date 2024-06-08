from django import forms
from .models import DietCalculator

class DietCalculatorForm(forms.ModelForm):
    class Meta:
        model = DietCalculator
        fields = ['weight', 'age', 'height', 'sex', 'activity', 'goal']