from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    last_updated_on = models.DateTimeField(default=timezone.now())
