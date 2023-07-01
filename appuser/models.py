from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # Custom fields
    points = models.IntegerField(default=0)
    task_completed = models.IntegerField(default=0)
    screenshot = models.ImageField(upload_to='screenshot_images/', null=True, blank=True)

    # Add any additional custom fields here

    def __str__(self):
        return self.username
