from models import Category


def get_categories_list():
    cats = Category.objects.filter(visible=True, superCategory=None)
    return_cat = []
    for cat in cats:
        tup = (cat, 0)
        return_cat.append(tup)
        get_cat_int(return_cat, cat, 1)
    return return_cat


def get_cat_int(ret_cat, cat, lvl):
    cats = Category.objects.filter(visible=True, superCategory=cat)
    for c in cats:
        tup = (c, lvl)
        ret_cat.append(tup)
        get_cat_int(ret_cat, c, lvl + 1)


