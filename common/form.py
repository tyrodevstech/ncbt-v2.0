from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','phone', 'address', 'desc']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name :'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email :'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone :'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address :'}),
            'desc': forms.Textarea(attrs={'placeholder': 'Message :','cols':'40','rows':'6'}),
        }