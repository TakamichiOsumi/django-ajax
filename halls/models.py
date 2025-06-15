from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    description = models.TextField(verbose_name = 'description',
                                   null = True,
                                   blank = True)
    class Meta:
        verbose_name_plural = 'CustomUser'

class Hall(models.Model):
    title = models.CharField(max_length = 255)
    user = models.ForeignKey('halls.CustomUser',
                             null = True,
                             blank = True,
                             on_delete = models.CASCADE)

class Video(models.Model):
    title = models.CharField(max_length = 255)
    url = models.URLField()
    youtube_id = models.CharField(max_length = 255)
    hall = models.ForeignKey(Hall, on_delete = models.CASCADE)
