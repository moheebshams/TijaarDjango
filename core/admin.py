from django.contrib import admin
from .models import*

# Hero Section
from .models import Slide

@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

# Category Section
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'products', 'icon')
    search_fields = ('name',)
    ordering = ('-id',)

# Featured Product
from .models import FeaturedProduct

@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'rating', 'reviews_count' , 'badge')

# Electronic Product
from .models import ElectronicsProduct

@admin.register(ElectronicsProduct)
class ElectronicsProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'rating', 'reviews_count', 'badge')
    list_filter = ('badge', 'rating')
    search_fields = ('name', 'description')
    ordering = ('-id',)

# Home Decor Product
from .models import HomeDecorProduct

@admin.register(HomeDecorProduct)
class HomeDecorProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'old_price', 'rating', 'reviews_count', 'badge')
    list_filter = ('badge', 'rating')
    search_fields = ('name', 'description')
    ordering = ('-id',)

# Customer Section
from .models import Customer, Stat

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'rating', 'time')
    search_fields = ('name', 'city', 'review')
    ordering = ('-id',)

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ('label', 'count', 'icon')
    search_fields = ('label',)

# Why Choose Us Section
from .models import WhyFeature

@admin.register(WhyFeature)
class WhyFeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')
    search_fields = ('title', 'description')
    ordering = ('id',)

# Special Offer Section
from django.contrib import admin
from .models import Offer

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'sale', 'discount', 'days', 'hours', 'minutes', 'start_time')
    search_fields = ('title', 'sale', 'discount', 'description')
    ordering = ('-id',)

# Wishlist
from .models import WishItem

@admin.register(WishItem)
class WishItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity')
    list_filter = ('user',)
