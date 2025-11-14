from django.db import models 
from django.core.validators import MinValueValidator
from slots.models import Slot 

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    person = models.PositiveIntegerField(validators=[MinValueValidator(1)], default = 1)
    slot = models.ForeignKey(Slot, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.email} X {self.slot.experience.title}"