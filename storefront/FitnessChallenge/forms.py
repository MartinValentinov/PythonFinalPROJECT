from django import forms
from .models import DietCalculator, CaloriesCalculator
from django.core.validators import EmailValidator

class DietCalculatorForm(forms.ModelForm):
    class Meta:
        model = DietCalculator
        fields = ['weight', 'age', 'height', 'sex', 'activity', 'goal']

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    email = forms.CharField(validators = [EmailValidator()])
    phone = forms.CharField(max_length = 10)
    subject = forms.CharField(max_length = 100)
    message = forms.CharField(widget = forms.Textarea)

class CalculatorForm(forms.ModelForm):
    class Meta:
        model = CaloriesCalculator
        fields = ['kilometers_ran', 'kilometers_walked']
