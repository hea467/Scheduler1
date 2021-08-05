from django.db import models

# Create your models here.
class Event(models.Model):
    description = models.CharField(max_length=150)
    start_time = models.DecimalField(max_digits=4, decimal_places=2)
    end_time = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.description
