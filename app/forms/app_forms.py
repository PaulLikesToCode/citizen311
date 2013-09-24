from django import forms
from django.contrib.auth.models import User
from app.models import Complaints

#User sign up form:
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

#User sign in form:
class SigninForm(forms.ModelForm):
    class Meta(object):
        model = User
        fields = ['username', 'password']
        widgets = {
            'password':forms.PasswordInput
        }

#Users comments form:
class CommentsForm(forms.Form):
    complaints = forms.CharField()
    comments = forms.CharField(widget=forms.Textarea)

#Look up a specific case:
class LookupForm(forms.ModelForm):
    class Meta(object):
        model = Complaints
        fields = ['case_id']

#User submit a case:
class SubmitForm(forms.Form):
    category = forms.CharField()
    address = forms.CharField()
    latitude = forms.CharField()
    longitude = forms.CharField()
    comments = forms.CharField(widget=forms.Textarea)