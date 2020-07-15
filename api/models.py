from django.db import models
from django.core.validators import MinLengthValidator


class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    env = models.CharField(max_length=20, blank=True)
    version = models.CharField(max_length=5, blank=True)
    address = models.GenericIPAddressField(
        protocol='IPv4', null=True, blank=True)


class Group(models.Model):
    name = models.CharField(max_length=50)


class User(models.Model):
    name = models.CharField(max_length=50)
    last_login = models.DateTimeField(null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=50, validators=[
                                MinLengthValidator(8)])
    groups = models.ManyToManyField(
        Group, related_name='users', through='GroupUser')


class GroupUser(models.Model):
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)


class Event(models.Model):
    LEVEL_CHOICES = [
        ('CRITICAL', 'Critical'),
        ('DEBUG', 'Debug'),
        ('ERROR', 'Error'),
        ('WARNING', 'Warning'),
        ('INFO', 'Info'),
    ]
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateField(auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
