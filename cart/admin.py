from django.contrib import admin
from .models import Cart, Order , Order_item,Customr_details

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display= ( 'user', 'is_ordered')
    list_display_links= ('user',)
    list_editable = ('is_ordered',)
    list_filter = ('user_id',)

admin.site.register(Cart,CartAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price')
    lsit_display_links = ('id',)
    

admin.site.register(Order, OrderAdmin)
admin.site.register(Customr_details)
admin.site.register(Order_item)