from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from basic_app import models

class SignUpForm(ModelForm):
    username = forms.CharField(max_length=20, validators=[MinLengthValidator(3)])
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, validators=[
        MinLengthValidator(8)
    ])

    class Meta:
        model = models.User
        fields = ('username', 'password', 'email') # all fields
        
class LoginForm(ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('username', 'password')

class CreatePostForm(ModelForm):
    content = forms.CharField(max_length=1024, widget=forms.Textarea)

    class Meta:
        model = models.Post
        fields = ('title', 'content')

class FeedbackForm(ModelForm):
    content = forms.CharField(max_length=1024, widget=forms.Textarea)

    class Meta:
        model = models.Feedback
        fields = ('content',)