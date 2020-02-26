from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator

from basic_app import models

class SignUpForm(ModelForm):
    # field requirements
    min_username_length = 3
    min_pass_length = 8

    username = forms.CharField(max_length=20, validators=[MinLengthValidator(min_username_length)])
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, validators=[
        MinLengthValidator(min_pass_length)
    ])
    verify_password = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('username', 'password', 'verify_password', 'email') # all fields

    # validate all of the user inputs
    def clean(self):
        # do not throw an error when cleaned_data key does not exist
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        verified_password = cleaned_data.get('verify_password')

        # verify password equals verified password
        if password != verified_password:
            raise forms.ValidationError(
                'Your password does not equal to the confirmed password!'
            )
        
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

class CommentPostForm(ModelForm):
    class Meta:
        model = models.Comment
        fields = ('post_commented', 'commenter', 'comment')