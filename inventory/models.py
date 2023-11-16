from django.db import models
import uuid

class Inventory(models.Model):
    inventory_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200,null=True,blank=True)
    iin = models.CharField(max_length=220,editable=False,unique=True)
    cost = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    profit_earned = models.IntegerField(default=0)
    revenue = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name

