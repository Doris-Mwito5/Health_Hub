
from django import forms
from .models import Consultation

class ConsultationForm(forms.ModelForm):
    class Meta:
        model = Consultation
        fields = ['name', 'email', 'phone', 'location']

# class ConsultationForm(forms.ModelForm):
#     class Meta:
#         model = Consultation
#         fields = ['name', 'email', 'phone', 'location']
