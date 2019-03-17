from django.forms import ModelForm, TextInput
from django import forms
from .models import City 

class CityForm(forms.ModelForm):
    class Meta:
        model = City 
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name','style': 'text-transform:uppercase;',})}

