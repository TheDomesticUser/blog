from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Feedback)