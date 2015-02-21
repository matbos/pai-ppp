from django.contrib import admin

from hurtownia.models import Item
from hurtownia.models import Category

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['name', 'description', 'category', 'lastModification', 'created', 'visible']
    # fields to filter the change list with
    list_filter = ['lastModification', 'created']
    # fields to search in change list
    search_fields = ['name', 'description', 'category']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True


admin.site.register(Item, ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'superCategory']
    save_on_top = True


admin.site.register(Category, CategoryAdmin)