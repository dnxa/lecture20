from django.db import models

# Create your models here.
class Robot(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    intelligence = models.IntegerField()