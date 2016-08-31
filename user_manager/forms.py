from django import forms


class LoginForm(forms.Form):
    id = forms.CharField(label="ID",max_length=12)
    password = forms.CharField(label="PASSWORD",max_length=12, widget=forms.PasswordInput)

class JoinForm(forms.Form):
    id = forms.CharField(label="ID",max_length=12,required=True)
    password = forms.CharField(label="PASSWORD", min_length=6, max_length=12, widget=forms.PasswordInput,required=True)
    password_check = forms.CharField(label="RE PASSWORD", min_length=6, max_length=12, widget=forms.PasswordInput,required=True)