import json

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import mail_admins, send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from items.models import Item

from .models import Cart, Customr_details, Order, Order_item


def cart(request):
    session_cart = request.session.get('cart')
    if request.user.is_authenticated:
        user = request.user.id
        cart = Cart.objects.all().filter(user=user, is_ordered=False).first()
    else:
        cart = Cart.objects.all().filter(pk=session_cart).first()
    context = {
        'cart': cart,
    }
    

    return render(request, 'cart.html', context)


def add_to_cart(request):
    cart_session = request.session.get('cart')

    item = Item.objects.get(pk=request.POST['item_id'])
    if request.user.is_authenticated:
        cart = Cart.objects.get_or_create(
            user=request.user, is_ordered=False)[0]
        cart_item = Order_item.objects.all().filter(
            item=item, shopping_cart=cart.id).first()
        if cart_item:
            cart_item.qty += 1
            cart_item.save()
            messages.success(request, 'cart updated')
        else:
            cart_item = Order_item(shopping_cart=cart, item=item)
            cart_item.save()
            cart.item.add(cart_item)
            cart.save()
            messages.success(request, 'Added to cart')
            print(cart.id)
    else:
        if cart_session:
            cart = Cart.objects.get(pk=cart_session)
            cart_item = Order_item.objects.all().filter(
                item=item, shopping_cart=cart_session).first()
            if cart_item:
                cart_item.qty += 1
                cart_item.save()
                messages.success(request, 'cart updated')
            else:
                cart_item = Order_item(shopping_cart=cart, item=item)
                cart_item.save()
                cart.item.add(cart_item)
                cart.save()
                messages.success(request, 'Added to cart')
                print(cart.id)
        else:
            cart = Cart()
            cart.save()
            cart_item = Order_item(shopping_cart=cart, item=item)
            cart_item.save()
            cart.item.add(cart_item)
            messages.success(request, 'Added to cart')
            request.session['cart'] = cart.id

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def remove_item(request):
    if request.method == 'POST':
        cart_item = Order_item.objects.get(pk=request.POST['cart_item'])
        if cart_item.qty == 1:
            cart_item.delete()
        else:
            cart_item.qty -= 1
            cart_item.save()
    messages.success(request, 'cart updated')
    return (redirect('cart'))


@login_required()
def check_out(request):
    cart = Cart.objects.all().filter(
        user_id=request.user.id, is_ordered=False).first()
    user = User.objects.get(pk=request.user.id)
    customer = Customr_details.objects.filter(user=user).first()
    if request.method == 'POST':
        if 'email' in request.POST:
            user = User(email=request.POST['email'])
        order = Order(customer=customer, cart=cart,
                      total_price=cart.cart_price())
        order.save()
        cart.is_ordered = True
        cart.save()

        # send_mail('Order Confirmation',
        #           'Your order has been confirmed successfully \n Thanks for shopping with us',
        #           settings.EMAIL_HOST_USER,
        #           [user.email])
        # mail_admins(
        #     subject='New Order !',
        #     message='We have recieved new order',
        #     fail_silently=False,
        #     connection=None,
        #     html_message=f'we recieved new order please check your admin pannel',
        # )
        messages.success(request, 'Your order has been confirmed')
        return redirect('index')

    else:
        user = User.objects.get(id=request.user.id)
        customer = Customr_details.objects.filter(user=user).first()
        context = {
            'cart': cart,
            'customer': customer
        }
    return render(request, 'checkout.html', context)


def customer_details(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        customer = Customr_details.objects.filter(user=request.user)
        if customer:
            customer.update(phone=phone, address=address)
        else:
            customer = Customr_details(
                user=request.user, address=address, phone=phone)
            customer.save()
        return redirect('check_out')
    else:
        pass
        # Todo

 # real time notification on admin pannel
 # export orders to csv files
 # sales informations (items, orders)
 # add real time updates to admin views
 # change order id generator

#  sales informations
# orders count , total sales , items sales
# create cart for anonymus user
