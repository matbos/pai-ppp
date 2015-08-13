from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'ProjektPPPPAI.views.home', name='home'),
                       url(r'.*.html', 'hurtownia.views.index'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^item/(?P<item>.+)', 'hurtownia.views.item_view'),
                       url(r'^category/(?P<cat_id>\d+)/(?P<cat_slug>.*)',
                           'hurtownia.views.category_view'),
                       url(r'^cart/add/(?P<item_id>\d+)/(?P<amount>\d+)/$',
                           'hurtownia.views.add_to_cart'),
                       url(r'^cart/remove/(?P<item_id>\d+)/$', 'hurtownia.views.remove_from_cart'),
                       url(r'^cart/remove/(?P<item_id>\d+)/(?P<amount>\d+)/$', 'hurtownia.views.remove_from_cart'),
                       url(r'^cart/$', 'hurtownia.views.cart_view'),
                       url(r'^login/$', 'django.contrib.auth.views.login',
                           {'template_name': 'hurtownia/login.html'}),
                       url(r'^logout/$', 'hurtownia.views.logout_view'),
                       url(r'^account/$', 'hurtownia.views.my_account'),
                       url(r'^account/password/', 'django.contrib.auth.views.password_change',
                           {'template_name': 'hurtownia/password.html',
                            'post_change_redirect': '/done/'}),
                       url(r'^done/', 'hurtownia.views.password_done'),
                       url(r'^account/(?P<action>.+)', 'hurtownia.views.account_change_view'),
                       url(r'^user/(?P<user_name>.+)', 'hurtownia.views.user_view'))

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))

urlpatterns += patterns('',
                        url(r'/', 'hurtownia.views.index'),
                        url(r'', 'hurtownia.views.index'))



