from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import  User
import uuid


# Create your models here.
class Cart(models.Model):
    item_id = models.IntegerField()
    item = models.CharField(max_length=200)
    user_id = models.IntegerField()
    is_ordered = models.BooleanField(default=False)
    price = models.FloatField()
    qty = models.IntegerField(default=1)

    def __str__(self):
        return self.item
    def total_price(self):
        return(self.price * self.qty )

class Customr_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)  
    def __str__(self):
        return str(self.user)

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default= uuid.uuid4,unique_for_date=True)
    cart = models.ManyToManyField(Cart)
    total_price = models.FloatField(blank=True)
    customer = models.ForeignKey(Customr_details, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

