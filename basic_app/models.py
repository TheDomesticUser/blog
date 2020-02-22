from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Regular users
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=256)
    last_login = models.DateField(null=True)
    profile_pic = models.ImageField(upload_to='profiles/', null=True, blank=True)
    desc = models.CharField(max_length=1024, default='', blank=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = [EMAIL_FIELD]

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)
    datetime_posted = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    post_commented = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_commented')
    comment = models.CharField(max_length=1024)
    datetime_commented = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.commenter.username + ': ' + str(self.date_commented)

class Feedback(models.Model):
    content = models.CharField(max_length=1024)
    datetime_sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.datetime_sent)

# Admins
class AdminPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.commenter