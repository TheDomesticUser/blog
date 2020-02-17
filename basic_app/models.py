from django.db import models

# Regular users
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=256)

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    message = models.CharField(max_length=2048)
    date_posted = models.DateField()

    def __str__(self):
        return self.commenter + ': ' + self.date_posted

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    post_commented = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_commented')
    message = models.CharField(max_length=1024)
    date_commented = models.DateField()

    def __str__(self):
        return self.author + ': ' + self.date_commented

# Admins
# class AdminPost(models.Model):
#     post = models.OneToOneField(Post, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.blog.commenter