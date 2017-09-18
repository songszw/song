from django.db import models
from django.contrib import admin


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    password = models.CharField(max_length=64)

class BlogsPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class BlogPostAdmin(admin.ModelAdmin):
    list_display=('title','timestamp')

admin.site.register(BlogsPost,BlogPostAdmin)