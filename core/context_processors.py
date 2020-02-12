from cart.models import Cart

def add_variable_to_context(request):
    
    session_cart = request.session.get('cart')
    if request.user.is_authenticated:
        user = request.user.id
        cart = Cart.objects.all().filter(user=user, is_ordered=False).first()
    else:
        cart = Cart.objects.all().filter(pk=session_cart).first()
    if cart:
        cart_count = cart.cart_count()
    else:
        cart_count = 0
    return {
        'test':'test',
        'count':cart_count
        }
    


