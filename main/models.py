from django.db import models

# Create your models here.
class Product(models.Model): 
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField() # tambahan
    condition = models.TextField() # used or new
    description = models.TextField() # tambahan
 