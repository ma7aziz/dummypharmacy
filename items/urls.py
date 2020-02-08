from django.urls import path
from . import views


urlpatterns = [
    path('search', views.search, name='search'),
    path('details/<int:item_id>', views.item_details, name='item_details')
]
