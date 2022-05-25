from statistics import mode
from django.db import models

# Create your models here.

class News(models.Model):
    #id will be genrate
    title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')
    reporterName = models.CharField(max_length=200,default='Anonymous')
    trp = models.IntegerField(null=True)

    class Meta:
        db_table = 'news'

