from django.db import models
from django.db.models import Sum
from django.contrib.auth.models import User
import uuid
from items.models import Item


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    item = models.ForeignKey('Order_item', on_delete=models.SET_NULL,null=True)
    is_ordered = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     unique_together = ('user', 'is_ordered',)
    def __str__(self):
        return str(self.user.username)

    def cart_price(self):
        prices = []
        for c in self.order_item_set.all():
            prices.append(c.total_price())
        return sum(prices)

    def cart_count(self):
        return self.order_item_set.all().count()


   

class Order_item(models.Model):
    shopping_cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    time = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.qty * self.item.price
    
    def __str__(self):
        return self.item.name


class Customr_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=500, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.user.username)


class Order(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique_for_date=True)
    cart = models.ForeignKey(Cart, on_delete=models.SET_NULL,null=True)
    total_price = models.FloatField(blank=True)
    customer = models.ForeignKey(
        Customr_details, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
