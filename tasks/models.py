from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    task_description = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
