from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=25)
    timestamp = models.IntegerField()
    value = models.FloatField()

    def __str__(self):
        return self.name
