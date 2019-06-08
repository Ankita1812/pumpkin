from django import forms
from .models import cityc


class PumpkinForm(forms.Form):
    city = forms.ChoiceField(choices=cityc, label='City')
    date = forms.DateTimeField(label='Date')
