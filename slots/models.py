from django.db import models
from django.core.validators import MinValueValidator
from experiences.models import Experience

# Create your models here.
class Slot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    availableSeats = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    total_seats = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.experience.title} X {self.date} X {self.time}"