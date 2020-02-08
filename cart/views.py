from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.core.mail import mail_admins, send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from items.models import Item
from .models import Cart, Customr_details, Order


@login_required
def add_to_cart(request):
    if request.method == 'POST':
        item_id = request.POST['item_id']
        user_id = request.POST['user_id']
        item = request.POST['item']
        price = request.POST['price']
        # check if item already in cart
        in_cart = Cart.objects.all().filter(
            user_id=user_id, item_id=item_id, is_ordered=False)
        if in_cart:
            item = Cart.objects.get(
                item_id=item_id, user_id=user_id, is_ordered=False)
            item.qty += 1
            item.save()
            messages.success(request, 'item added to cart!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            cart_item = Cart(item_id=item_id, user_id=user_id,
                             item=item, price=price)
            cart_item.save()
            messages.success(request, 'item added to cart!')
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return redirect('index')


def cart(request):
    user_id = request.user.id
    cart_items = Cart.objects.all().filter(user_id=user_id, is_ordered=False)
    prices = []

    for item in cart_items:
        prices.append(item.price * item.qty)

    context = {
        'items': cart_items,
        'total_price': sum(prices)
    }
    request.session['prices'] = prices
    return render(request, 'cart.html', context)


def remove_item(request):
    if request.method == 'POST':

        item_id = request.POST['item_id']
        user_id = request.POST['user_id']
        quantity = request.POST['quantity']
        item = Cart.objects.get(
            user_id=user_id, item_id=item_id, is_ordered=False)
        if item.qty == 1:
            item.delete()
        else:
            item.qty -= 1
            item.save()
    messages.success(request, 'cart updated')
    return (redirect('cart'))


def check_out(request):
    cart_items = Cart.objects.all().filter(
        user_id=request.user.id, is_ordered=False)
    prices = request.session.get('prices')
    user = User.objects.get(pk=request.user.id)
    customer = Customr_details.objects.filter(user=user).first()
    if request.method == 'POST':
        if 'email' in request.POST:
            user = User(email=request.POST['email'])
        order = Order(customer=customer, total_price=sum(prices))
        order.save()
        for cart in cart_items:
            cart.is_ordered = True
            cart.save()
            order.cart.add(cart)
            item = Item.objects.get(pk=cart.item_id)
            item.times_sold += cart.qty 
            item.save()
        send_mail('Order Confirmation',
                  'Your order has been confirmed successfully \n Thanks for shopping with us',
                  settings.EMAIL_HOST_USER,
                  [user.email])
        mail_admins(
            subject='New Order !',
            message='We have recieved new order',
            fail_silently=False,
            connection=None,
            html_message=f'we recieved new order please check your admin pannel',
        )
        messages.success(request, 'Your order has been confirmed')
        return redirect('index')

    else:
        user = User.objects.get(id=request.user.id)
        customer = Customr_details.objects.filter(user=user).first()
        context = {
            'items': cart_items,
            'total_price': sum(prices),
            'count': cart_items.count(),
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
