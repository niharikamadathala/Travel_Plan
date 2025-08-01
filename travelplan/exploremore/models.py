from django.db import models

# Create your models here.

class ExploreMore(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='places_images/')
    description = models.TextField()

    def __str__(self):
        return self.name
