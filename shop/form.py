from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import Address
class CustomUserForm(UserCreationForm):#It will Inherits an UserCreationFrom from Django
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the UserName'}))#attrs are the Attributes Short Form
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the E-mail'}))#attrs are the Attributes Short Form
    mob=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the Mob-Num'}),min_length=2)#attrs are the Attributes Short Form
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the Password'}))#attrs are the Attributes Short Form
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Retype The Password'}))#attrs are the Attributes Short Form
    class Meta:
        model=User
        fields=['username','email','mob','password1','password2']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['full_name', 'phone', 'email', 'address', 'city', 'state', 'pincode']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control'}),
        }




