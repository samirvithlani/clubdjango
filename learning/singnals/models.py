from django.db.models import signals
from django.db import models
from django.dispatch import receiver


# Create your models here.
class eProduct(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(null=False)
    description = models.TextField()
    pub_date = models.DateTimeField('date published')

    class Meta:
        db_table = 'eProducts'

@receiver(signals.post_save,sender=eProduct)
def create_product(sender,instance,created,**kwargs):
    print('Product Created')
    print(instance)
    print(created)
    print(kwargs)
    print(sender)

@receiver(signals.pre_save,sender=eProduct)
def before_create_product(sender,instance,**kwargs):
    print('Before Product Created')
    print(instance)
    print(kwargs)
    print(sender)    

    
    
        