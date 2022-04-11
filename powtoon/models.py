from django.contrib.auth.models import AbstractUser
from django.db import models


class Powtoon(models.Model):
    name = models.CharField(max_length=255)
    contentJson = models.JSONField(default=dict)
    owner = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, related_name='owner_of')
    sharedWith = models.ManyToManyField('User', related_name='shared_with_user', blank=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    pass


class Permission(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    permission = models.ManyToManyField('Permission')

    def __str__(self):
        return self.name
