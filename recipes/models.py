from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    cook = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Magic method to have a printable object"""

        return self.title 


