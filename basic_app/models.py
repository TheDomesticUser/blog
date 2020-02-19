from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Regular users
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=256)
    last_login = models.DateField(null=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    REQUIRED_FIELDS = [EMAIL_FIELD]

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.CharField(max_length=2048)
    date_posted = models.DateField()

    def __str__(self):
        return self.author + ': ' + self.date_posted

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    post_commented = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_commented')
    comment = models.CharField(max_length=1024)
    date_commented = models.DateField()

    def __str__(self):
        return self.commenter + ': ' + self.date_commented

# Admins
# class AdminPost(models.Model):
#     post = models.OneToOneField(Post, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.blog.commenter