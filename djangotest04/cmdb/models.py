from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_group = models.ForeignKey('UserGroup',to_field='uid',default=1)


class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption = models.CharField(max_length=32,unique=True)
    time = models.DateTimeField(auto_now=True,null=True)
