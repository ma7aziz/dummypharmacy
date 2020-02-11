from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import SignUpForm

from cart.models import Order, Customr_details, Cart, Order_item
from items.models import Item,CATEGORY_CHOICES


# Create your views here.


def index(request):
    items = Item.objects.all().order_by('-price')
    recent = Item.objects.all().order_by('-created')[:5]
    top_selling = Item.objects.all().order_by('-times_sold')[:5]
    cart_session = request.session.get('cart')
    if request.user.is_authenticated:
        if cart_session:
            cart = Cart.objects.get(pk=cart_session)
            user = User.objects.get(pk= request.user.id)
            cart.user = user
            cart.save()
            user_carts = Cart.objects.all().filter(user = user, is_ordered=False)
            
            if len(user_carts) == 2:
                for item in user_carts[0].item.all():
                  item.shopping_cart.id = user_carts[1].id
                  item.save()
                  user_carts[1].save()
                user_carts[0].delete()
            
                    
    context = {
        'items': items,
        'recent': recent,
        'top_selling': top_selling,
        'categories': CATEGORY_CHOICES
    }
    return render(request, 'index.html', context)


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})





@user_passes_test(lambda u: u.is_superuser)
def orders(request):
    orders = Order.objects.all().order_by('-order_date')


    return render(request, 'orders.html', {'orders': orders})


def category(request, category):
    items = Item.objects.all().filter(category=category)
    return render(request, 'category.html', {'items':items, 'category':category, 'categories': CATEGORY_CHOICES})