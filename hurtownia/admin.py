from django.contrib import admin

from hurtownia.models import Item
from hurtownia.models import Category

from hurtownia.models import Photo

# Register your models here.

class InlineImage(admin.TabularInline):
    model = Photo


class ItemAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['name', 'description', 'category', 'lastModification', 'created', 'visible',
                    'creator']
    # fields to filter the change list with
    list_filter = ['lastModification', 'created', 'creator']
    # fields to search in change list
    search_fields = ['name', 'description', 'category', 'creator']
    # enable the date drill down on change list
    date_hierarchy = 'created'
    # enable the save buttons on top on change form
    save_on_top = True
    inlines = [InlineImage]


admin.site.register(Item, ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'superCategory']
    save_on_top = True


admin.site.register(Category, CategoryAdmin)

admin.site.register(Photo)