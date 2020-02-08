from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index' ),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('category/<category>', views.category, name='category'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('orders', views.orders, name='orders')
]
