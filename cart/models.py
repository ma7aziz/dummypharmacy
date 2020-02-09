from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
import uuid
from items.models import Item


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    qty = models.IntegerField(default=1)
    
    def __str__(self):
        return self.item.name

    def total_price(self):
        return self.qty * self.item.price


class Customr_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique_for_date=True)
    cart = models.ManyToManyField(Cart)
    total_price = models.FloatField(blank=True)
    customer = models.ForeignKey(
        Customr_details, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
