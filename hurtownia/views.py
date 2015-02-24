from django.shortcuts import render

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

from models import Item
from models import Category
from helper import get_categories_list
from ItemHelper import get_listing_by_category

# Create your views here.

def index(request):
    return render(request, 'hurtownia/index.html',
                  {'items': Item.objects.filter(visible=True),
                   'categories': get_categories_list(),
                   'title': "Super Shops - Shop Listings"})


def item_view(request, item):
    # get the Post object
    itemResponse = get_object_or_404(Item, slug=item)
    # now return the rendered template
    return render(request, 'hurtownia/item.html',
                  {'item': itemResponse,
                   'categories': get_categories_list()})


def category_view(request, cat_id, cat_slug):
    cat = get_object_or_404(Category, id=cat_id)
    # now return the rendered template
    return render(request, 'hurtownia/category.html',
                  {'category': cat,
                   'items': get_listing_by_category(cat),
                   'categories': get_categories_list()})


def login_view(request):
    return login(request, template_name='hurtownia/login.html')


def logout_view(request):
    logout(request)
    # now return the rendered template
    return render(request, 'hurtownia/logout.html',
                  {'items': Item.objects.filter(visible=True),
                   'categories': get_categories_list(),
                   'title': "Super Shops - Shop Listings"})


@login_required(login_url='/login/')
def my_account(request):
    return render(request, 'hurtownia/my_acc.html',
                  {'categories': get_categories_list(), })


@login_required(login_url='/login/')
def password_done(request):
    return render(request, 'hurtownia/my_acc.html',
                  {'categories': get_categories_list(),
                   'message': 'Your password has been set!',
                   'message_class': 'positive'})


@login_required(login_url='/login/')
def account_change_view(request, action):
    if request.method == 'GET':

        return render(request, 'hurtownia/change.html',
                      {'label': 'New ' + action,
                       'what': action,
                       'categories': get_categories_list()})
    elif request.method == 'POST':
        val = request.POST['newValue']
        action = request.POST['what']
        if action == 'first_name':
            request.user.first_name = val
        elif action == 'last_name':
            request.user.last_name = val
        elif action == 'email':
            request.user.email = val
        request.user.save()
        return my_account(request)


def user_view(request, user_name):
    # get the Post object
    # itemResponse = get_object_or_404(Item, name=item)
    # req_user = User.find
    # now return the rendered template
    return render(request, 'hurtownia/user.html',
                  {'categories': get_categories_list()})


def cart_view(request):
    if request.session.__contains__('cart'):

        session_cart = request.session['cart']
        temp_cart = []
        cart = []
        if session_cart:
            temp_cart = breakdown_list_to_map(session_cart)
        if temp_cart:
            for t in temp_cart:
                cart.append((Item.objects.filter(id=t[0])[0], t[1]))

        return render(request, 'hurtownia/cart.html',
                      {'cart': cart})
    else:
        return redirect(request.META['HTTP_REFERER'])


def remove_from_cart(request, item_id, amount=0):
    iamount = int(amount)
    litem_id = long(item_id)
    session_cart = request.session['cart']
    temp_cart = []
    if session_cart:
        temp_cart = breakdown_list_to_map(session_cart)
        if iamount == 0:
            temp_cart = remove_from_list_by_id(temp_cart, litem_id)
        else:
            temp_cart = remove_from_list_with_amount(temp_cart, litem_id, iamount)
        request.session['cart'] = temp_cart
    return redirect(request.META['HTTP_REFERER'])


def remove_from_list_with_amount(cart, item_id, amount):
    old_t = ()
    for t in cart:
        if t[0] == item_id:
            old_t = t
    if old_t:
        cart.remove(old_t)
    if old_t[1] > amount:
        cart.append((old_t[0], old_t[1] - amount))
    return map_to_list(cart)


def add_to_cart(request, item_id, amount):
    iamount = int(amount)
    litem_id = long(item_id)
    if not request.session.__contains__('cart'):
        request.session['cart'] = [litem_id, iamount]
    else:
        request.session['cart'] = add_to_list(request.session['cart'], litem_id, iamount)
    return redirect(request.META['HTTP_REFERER'])


def remove_from_list_by_id(my_map, my_id):
    old_t = ()
    for t in my_map:
        if t[0] == my_id:
            old_t = t
    if old_t:
        my_map.remove(old_t)
    return map_to_list(my_map)


def add_to_list(session_list, item, amount):
    my_map = breakdown_list_to_map(session_list)
    old_t = ()
    for t in my_map:
        if t[0] == item:
            old_t = t
    if old_t:
        my_map.remove(old_t)
    else:
        old_t = (item, 0)
    my_map.append((old_t[0], old_t[1] + amount))

    return map_to_list(my_map)


def breakdown_list_to_map(flat_map):
    normal_map = []
    length = len(flat_map)
    i = 0
    while i < length:
        normal_map.append((flat_map[i], flat_map[i + 1]))
        i += 2
    return normal_map


def map_to_list(normal_map):
    flatten_map = []
    for t in normal_map:
        flatten_map.append(t[0])
        flatten_map.append(t[1])
    return flatten_map

