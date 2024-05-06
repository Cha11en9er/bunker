from django import forms

class LoginUser(forms.Form):
    login = forms.CharField(max_length=30)
    email = forms.EmailField()
    