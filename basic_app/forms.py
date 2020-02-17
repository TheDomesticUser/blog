from django.forms import ModelForm
from django import forms
from .models import User, Post, Comment
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

class SignUpForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, validators=[
        MinLengthValidator(8)
    ])

    class Meta:
        model = User
        fields = ('username', 'password', 'email') # all fields