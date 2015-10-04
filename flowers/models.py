from django.db import models
from django.utils import timezone

# Create your models here.

class Flower(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.IntegerField()
    pic = models.ImageField(upload_to="media/flower_pics/%Y/%m/%d")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
