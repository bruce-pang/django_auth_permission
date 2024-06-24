from django.db import models
from django.contrib.auth.models import AbstractUser

class OwnUser(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='手机号')
    age = models.IntegerField(verbose_name='年龄', default=18)
