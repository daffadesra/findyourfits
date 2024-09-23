import uuid
from django.db import models
# Tugas 4
from django.contrib.auth.models import User

# Create your models here.
class ProductEntry(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    stock = models.IntegerField() # tambahan
    condition = models.TextField() # used or new
    description = models.TextField() # tambahan
 