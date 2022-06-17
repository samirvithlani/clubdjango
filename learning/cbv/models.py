from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    capital = models.CharField(max_length=100)

    class Meta:
        db_table='country'
    
