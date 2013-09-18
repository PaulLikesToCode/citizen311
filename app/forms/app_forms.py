from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            "password":forms.PasswordInput
        }

class SignupConfirmForm(SignupForm):
    confirm_password = forms.CharField(
        widget = forms.PasswordInput
    )
    def clean(self):
        password = self.cleaned_data.get('password')
        password_conf = self.cleaned_data.get("confirm_password")
        if password is not None and password != password_conf:
            raise forms.ValidationError(
                "Password confirmation does not match password."
            )
        return self.cleaned_data

class SigninForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ['username', 'password']
        widgets = {
            'password':forms.PasswordInput
        }

class CommentsForm(forms.Form):
    username = forms.CharField()
    complaints = forms.CharField()
    comments = forms.CharField(widget=forms.Textarea)
