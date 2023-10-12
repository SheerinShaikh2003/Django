from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default='1'
    )
    prod_code =models.IntegerField(default=100)
    for_user = models.CharField(
        max_length=100,
        default='xyz'
    )
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(
        max_length=500,
        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Eaque, reiciendis saepe accusantium fugiat illo reprehenderit quidoloribus molestiae recusandae? Recusandae ducimus accusamus et. Soluta asperiores rerum laboriosam ratione, rem sed."
        )
    item_price = models.IntegerField()
    item_image = models.CharField(
      max_length=500,
      default="https://cdn-icons-png.flaticon.com/512/1377/1377194.png")
    
    def __str__(self):
        return self.item_name
