from django.urls import path
from . import views

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
