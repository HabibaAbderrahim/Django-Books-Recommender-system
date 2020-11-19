from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from django import forms
from django.contrib.auth import authenticate , login
from django.contrib.auth.models import  User
from django.contrib.auth import authenticate , login

class RegisterForm(UserCreationForm) :

    email = forms.EmailField(required=True)

    class Meta :
        model = User
        fields = ["username","email","password1","password2"]
    def clean_email(self):
        email_address = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email_address)
        if qs.exists():
            raise forms.ValidationError("The email address you've chosen is already registered.")
        return email_address


class UserLoginForm(forms.Form):
    username = forms.CharField(label="")
    password =  forms.CharField(label="",widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

