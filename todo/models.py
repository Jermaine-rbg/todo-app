from django.db import models

# Create your models here.

class Task(models.Model):
    # An ID field is automatically added to all Django models
    description = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

class Note(models.Model):
    text = models.CharField(max_length=255)