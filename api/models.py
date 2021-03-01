from django.db import models

# Create your models here.
class Marks(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField(primary_key=True)
    chemistry = models.FloatField()
    maths = models.FloatField()
    physics = models.FloatField()
    total = models.FloatField(default=0.0)
    percent = models.FloatField(default=0.0)