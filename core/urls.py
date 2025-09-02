from django.contrib import admin

from django.urls import path
from core import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('header/', views.header, name='header'),
    path('hero/', views.hero, name='hero'),
    path('category/', views.category, name='category'),
    path('featured/', views.featured, name='featured'),
    path('electronics/', views.electronics, name='electronics'),
    path('decor/', views.decor, name='decor'),
    path('customer/', views.customer, name='customer'),
    path('why/', views.why, name='why'),
    path('offer/', views.offer, name='offer'),
    path('footer/', views.footer, name='footer'),

    path('addToCart/', views.addToCart, name='addToCart'),
    path('form/', views.form, name='form'),
    path('trackYourOrder/', views.trackYourOrder, name='trackYourOrder'),
    path('categories/', views.categories, name='categories'),
    path('products/', views.products, name='products'),
    path('productDetail/', views.productDetail, name='productDetail'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)