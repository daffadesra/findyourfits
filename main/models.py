import uuid
from django.db import models

# Create your models here.
class ProductEntry(models.Model): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField() # tambahan
    condition = models.TextField() # used or new
    description = models.TextField() # tambahan
 