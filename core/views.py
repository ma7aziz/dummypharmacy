from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


from cart.models import Order
from items.models import Item,CATEGORY_CHOICES


# Create your views here.


def index(request):
    print(request.session.keys())
    items = Item.objects.all().order_by('-price')
    recent = Item.objects.all().order_by('-created')[:5]
    top_selling = Item.objects.all().order_by('-times_sold')[:5]

    context = {
        'items': items,
        'recent': recent,
        'top_selling': top_selling,
        'categories': CATEGORY_CHOICES
    }
    return render(request, 'index.html', context)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")

            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


def profile(request):
    # Add details and order history
    return render(request, 'profile.html')


@user_passes_test(lambda u: u.is_superuser)
def orders(request):
    orders = Order.objects.all().order_by('-order_date')
    return render(request, 'orders.html', {'orders': orders})


def category(request, category):

    items = Item.objects.all().filter(category=category)
    return render(request, 'category.html', {'items':items, 'category':category, 'categories': CATEGORY_CHOICES})