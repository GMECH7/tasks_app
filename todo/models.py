from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = (
        ("open", "OPEN"),
        ("closed", "CLOSED"),
        ("withdrew", "WITHDREW"),
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="open")
    description = models.TextField()
    date_created = models.DateField(default=timezone.now)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.description
