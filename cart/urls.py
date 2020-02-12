from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart, name='cart'),
    path('add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('remove_item', views.remove_item, name='remove_item'),
    path('check_out', views.check_out, name='check_out'),
    path('customr_details', views.customer_details, name='customer_details'),
    path('clear_cart/<int:cart_id>', views.clear_cart, name='clear_cart'),
    

]
