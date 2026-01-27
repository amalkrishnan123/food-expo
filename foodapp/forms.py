from django import forms
from .models import Registration
from .models import Partners

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = ['name', 'email', 'mobile', 'address']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'mobile', 'address', 'category']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Full Name',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email Address',
                'class': 'form-control'
            }),
            'mobile': forms.TextInput(attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                'placeholder': 'Address',
                'rows': 3,
                'class': 'form-control'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
        }
