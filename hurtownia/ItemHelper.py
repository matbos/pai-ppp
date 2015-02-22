from hurtownia.models import Item, Category


def get_listing_by_category(category):
    cats = get_all_subcategories(category)
    if not cats:
        cats.append(category)
    listings = Item.objects.filter(category__in=cats, visible=True)
    return listings


def get_all_subcategories(category):
    cats = Category.objects.filter(superCategory=category)
    cats_list = []
    if cats:
        for cat in cats:
            cats_list.append(cat)
            get_subcat_int(cat, cats_list)
    return cats_list


def get_subcat_int(category, cats_list):
    cats = Category.objects.filter(superCategory=category)
    for cat in cats:
        cats_list.append(cat)
        get_subcat_int(cat, cats)


