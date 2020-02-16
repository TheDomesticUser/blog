from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.username

class Blog(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    message = models.CharField(max_length=2048)
    date_posted = models.DateField()

    def __str__(self):
        return self.commenter + ': ' + self.date_posted