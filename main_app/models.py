from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Goal(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=100)
  determination = models.IntegerField(
    validators=[
      MaxValueValidator(7),
      MinValueValidator(1)
    ]
  )

  def __str__(self):
    return self.name