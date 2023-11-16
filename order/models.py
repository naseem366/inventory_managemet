from django.db import models
from inventory.models import *

# Create your models here.


class Orders(models.Model):
    order_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200,null=True,blank=True,)
    item = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)
    orderdttm = models.DateTimeField(auto_now_add = True)
    is_received = models.BooleanField(default=False)
    is_cancel = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    transaction_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200, null=True,blank=True,)
    item = models.ForeignKey(Inventory,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    selling_price = models.IntegerField(default=0)
    transactiondttm = models.DateTimeField(auto_now_add = True)
    

    def __str__(self):
        return self.name
