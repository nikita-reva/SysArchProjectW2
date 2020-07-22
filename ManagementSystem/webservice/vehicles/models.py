from django.db import models
from PIL import Image

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    driver = models.CharField(max_length=100, default='None')
    description = models.TextField()
    image = models.ImageField(default='default_car.png', upload_to='vehicle_pics')

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        super(Vehicle, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 300:
            output_size = (200, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
