from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'times_sold', 'created','category', 'published')
    list_display_links = ('name', )
    list_filter = ('name', 'published', 'category')                      #category TODO
    list_per_page = 25
    list_editable = ('published', 'price', 'category')




admin.site.register(Item, ItemAdmin)