from django import forms
from .models import PIDData

class PIDDataForm(forms.ModelForm):
    class Meta:
        model = PIDData
        fields = '__all__'
