from django.db import models

# Create your models here.
class Experience(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.PositiveIntegerField()
    image_url = models.CharField()

    def __str__(self):
        return self.title 