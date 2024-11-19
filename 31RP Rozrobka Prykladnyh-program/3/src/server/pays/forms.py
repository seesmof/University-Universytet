from django import forms

class Login(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())