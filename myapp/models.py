from django.db import models

# Create your models here.
class Profile(models.Model):
    date = models.DateField(default='', verbose_name='date')
