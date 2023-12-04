from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    TYPE_CHOICES = (
        ("py", "Python programming"),
        ("cpp", "C++ programming"),
        ("mldl", "ML/DL"),
        ("django", "django web development"),
        ("study", "Studying"),
        ("trade", "Trading"),
        ("fluid", "Fluid dynamics"),
        ("thermodynamics", "Thermodynamics"),
        ("maths", "Mathematics"),
        ("ices", "ICEs"),
        ("other", "Other"),
    )

    STATUS_CHOICES = (
        ("open", "OPEN"),
        ("closed", "CLOSED"),
        ("withdrew", "WITHDREW"),
    )

    task_type_1 = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default="other", blank=True
    )
    task_type_2 = models.CharField(
        max_length=100, choices=TYPE_CHOICES, default="other", blank=True
    )
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default="open")
    description = models.TextField()
    date_created = models.DateField(default=timezone.now)
    date_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.description
