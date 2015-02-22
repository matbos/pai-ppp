from django.shortcuts import render
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

