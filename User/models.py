from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Users(AbstractUser):
    """
    继承Django的User类
    """
    CHOICES = (
        ('yes', 'Yes'),
        ('no', 'NO'),
    )
    is_professional = models.CharField(choices=CHOICES, max_length=4)
    photo = models.ImageField('头像',default='static/images/user_protrait/portrait.jpg.jpg')
