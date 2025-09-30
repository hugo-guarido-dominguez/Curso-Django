from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from datetime import timedelta

# Create your models here.
class Destination(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    travel_time = models.DurationField(
        null=False,
        blank=False,
        default=timedelta(days=1),
        help_text="Approximate travel time"
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("destination_detail", kwargs={"pk": self.pk})
    
class Cruise(models.Model):
    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=50
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )
    passengers = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    destinations = models.ManyToManyField(
        Destination,
        related_name="cruises"
    )

    def __str__(self):
        return self.name