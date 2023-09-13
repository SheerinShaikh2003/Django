
from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=300)
    item_price = models.IntegerField()
    item_image = models.CharField(
      max_length=500,
      default="https://cdn-icons-png.flaticon.com/512/1377/1377194.png")
    
    def _str_(self):
        return self.item_name
