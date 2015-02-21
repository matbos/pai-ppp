from django.shortcuts import render
from django.shortcuts import get_object_or_404

from models import Item

# Create your views here.

def index(request):
    # get the blog posts that are published
    items = Item.objects.filter(visible=True)
    # now return the rendered template
    return render(request, 'hurtownia/index.html', {'items': items})


def item(request, item):
    # get the Post object
    itemResponse = get_object_or_404(Item, name=item)
    # now return the rendered template
    return render(request, 'hurtownia/item.html', {'item': itemResponse})