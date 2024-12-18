from django.http import HttpRequest
from django.views.generic import ListView
from .models import *
from django.shortcuts import redirect, render
from .forms import OrderForm
from django.contrib import messages


class RimsView(ListView):
    model = Rims
    paginate_by = 4
    template_name = 'blog/rims.html'
    context_object_name = 'rims'


class SparesView(ListView):
    model = Spares
    paginate_by = 4
    template_name = 'blog/spares.html'
    context_object_name = 'spares'


def index_view(request):
    return render(request, 'blog/index.html')


def cart_add(request, rims_id):
    if not request.user.is_authenticated:
        return redirect('login_page')

    if request.method == 'POST':
        rims = Rims.objects.get(id=rims_id)
        carts = Cart.objects.filter(user=request.user, rims=rims)

        if carts.exists():
            cart = carts.first()
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(user=request.user, rims=rims, quantity=1)

    return redirect('cart')


def get_cart(request):
    if not request.user.is_authenticated:
        return redirect('login_page')

    rims_cart = Cart.objects.filter(user=request.user, rims__isnull=False)
    spares_cart = Cart.objects.filter(user=request.user, spares__isnull=False)
    context = {
        'rims_cart': rims_cart,
        'spares_cart': spares_cart
    }
    return render(request, 'blog/cart.html', context)


def delete_card(request, cart_id):
    if not request.user.is_authenticated:
        return redirect('login_page')
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect('cart')


def spares_add_to_cart(request, spare_id):
    if not request.user.is_authenticated:
        return redirect('login_page')

    if request.method == 'POST':
        spare = Spares.objects.get(id=spare_id)
        cart = Cart.objects.filter(user=request.user, spares=spare)

        if cart.exists():
            carts = cart.first()
            carts.quantity += 1
            carts.save()
        else:
            Cart.objects.create(user=request.user, spares=spare, quantity=1)
    return redirect('cart')


def update_item_quantity(request, cart_id: int, quantity: int):
    if not request.user.is_authenticated:
        return redirect('login_page')

    item = Cart.objects.filter(id=cart_id, user__id=request.user.id)
    if not item.exists():
        return redirect('cart')
    
    item = item.first()
    item.quantity = quantity
    item.save()

    return redirect('cart')


def buy_items(request: HttpRequest, cart_id: int = None):
    if not request.user.is_authenticated:
        return redirect('login_page')
    
    context = {
        'rims': [],
        'spares': [],
        'form': OrderForm(),
        'cart_id': cart_id,
    }

    if cart_id:
        items = Cart.objects.filter(id=cart_id, user__id=request.user.id)
        if not items.exists():
            return redirect('cart')
        
        item = items.first()
        if item.rims:
            context['rims'] = [item]
        else:
            context['spares'] = [item]
    else:
        context['rims'] = Cart.objects.filter(user__id=request.user.id, rims__isnull=False, spares__isnull=True)
        context['spares'] = Cart.objects.filter(user__id=request.user.id, rims__isnull=True, spares__isnull=False)


    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order_items = [
                *[
                    OrderItem.objects.create(
                        quantity=item.quantity,
                        rims=item.rims,
                    ) for item in context['rims']
                ],
                *[
                    OrderItem.objects.create(
                        quantity=item.quantity,
                        spares=item.spares,
                    ) for item in context['spares']
                ]
            ]
            order = Order.objects.create(
                **form.cleaned_data,
                user=request.user,
            )
            order.items.set(order_items)
            return redirect('make-order', order_id=order.id)

        context['form'] = form

    return render(request, 'blog/order.html', context=context)

    

def make_order(request: HttpRequest, order_id: int):
    if not request.user.is_authenticated:
        return redirect('login_page')

    order = Order.objects.get(id=order_id, user__id=request.user.id)
    rims_order_items = order.items.filter(rims__isnull=False, spares__isnull=True)
    spares_order_items = order.items.filter(spares__isnull=False, rims__isnull=True)

    Cart.objects.filter(rims__id__in=[rim.rims.id for rim in rims_order_items]).delete()
    Cart.objects.filter(spares__in=[spare.spares.id for spare in spares_order_items]).delete()
    
    messages.success(request, "Заказ успешно создан! Оператор скоро свяжется с Вами для уточнения деталей доставки.")
    return redirect('cart')


    