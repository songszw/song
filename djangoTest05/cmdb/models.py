from django.db import models

# Create your models here.

class Busniess(models.Model):
    caption = models.CharField(max_length=32)
    code = models.CharField(max_length=32)

class Host(models.Model):
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32,db_index=True)
    ip = models.GenericIPAddressField(db_index=True)
    port = models.IntegerField()
    b = models.ForeignKey('Busniess',to_field='id')


class Application(models.Model):
    name=  models.CharField(max_length=32)
    r = models.ManyToManyField('Host')

























