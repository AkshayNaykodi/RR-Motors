from django.contrib import admin
from django.urls import path
from rr_app import views
from django.conf.urls.static import static
from rr import settings



urlpatterns = [
    path('home',views.home),
    path('login',views.user_login),
    path('pdetails/<pid>',views.pdetails),
    path('products',views.products),
    path('contact',views.contact),
    path('register',views.register),
    path('logout',views.user_logout),
    path('catfilter/<cv>',views.catfilter),
    path('sort/<sv>',views.sort),
    path('range',views.range),
    path('addtocart/<pid>',views.addtocart),
    path('viewcart',views.viewcart),
    path('remove/<cid>',views.remove),
    path('updateqty/<qv>/<cid>',views.updateqty),
    path('placeorder',views.placeorder),
    path('removeorder/<oid>',views.removeorder),
    path('makepayment',views.makepayment),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)