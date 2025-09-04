from django.db import models


# Desktop slider
class Slide(models.Model):
    title = models.CharField(max_length=100, blank=True)
    subtitle = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='slides/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title or f"Slide {self.id}"

# Category Section
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class, e.g., fa-couch")
    products = models.PositiveIntegerField(default=0, help_text="Number of products in this category")
    
    def __str__(self):
        return self.name

# Featured Products
class FeaturedProduct(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='featured/')
    price = models.CharField(max_length=20)
    old_price = models.CharField(max_length=20, blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    badge = models.CharField(max_length=20, blank=True, null=True)
    rating = models.PositiveIntegerField(default=0)
    reviews_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# Electronic Products
class ElectronicsProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='electronics/')
    price = models.CharField(max_length=20)
    old_price = models.CharField(max_length=20, blank=True, null=True)
    badge = models.CharField(max_length=50, null=True, blank=True)
    rating = models.PositiveIntegerField(default=0)
    reviews_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# Home Decor Products
class HomeDecorProduct(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='home_decor/')
    price = models.CharField(max_length=20)
    old_price = models.CharField(max_length=20, blank=True, null=True)
    badge = models.CharField(max_length=50, null=True, blank=True)
    rating = models.PositiveIntegerField(default=0)
    reviews_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

# Customer Section
class Customer(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='customers/')  # store profile images
    review = models.TextField()
    rating = models.FloatField(default=5.0, help_text="Rating out of 5 (e.g., 4.5)")
    time = models.CharField(max_length=50, help_text="e.g., '2 days ago'")

    @property
    def stars(self):
        """
        Returns a list like [1, 1, 1, 0.5, 0] based on rating (supports half stars).
        """
        stars = []
        remaining = self.rating
        for _ in range(5):
            if remaining >= 1:
                stars.append(1)
                remaining -= 1
            elif remaining >= 0.5:
                stars.append(0.5)
                remaining -= 0.5
            else:
                stars.append(0)
        return stars

    def __str__(self):
        return self.name


class Stat(models.Model):
    label = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    icon = models.CharField(max_length=100, help_text="Font Awesome class (e.g., fa-users)")

    def __str__(self):
        return self.label

# Why Choose Us
class WhyFeature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Font Awesome class (e.g., fa-shipping-fast)")

    class Meta:
        verbose_name = "Why Choose Tijaar Feature"
        verbose_name_plural = "Why Choose Tijaar Features"
        ordering = ['id']  # To maintain the order they are added

    def __str__(self):
        return self.title

# Special offer
from django.utils import timezone
from datetime import timedelta

class Offer(models.Model):
    title = models.CharField(max_length=100)
    sale = models.CharField(max_length=100)
    discount = models.CharField(max_length=100)
    description = models.TextField()
    days = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    image = models.ImageField(upload_to='offers/')
    start_time = models.DateTimeField(default=timezone.now)

    @property
    def end_time(self):
        return self.start_time + timedelta(
            days=self.days, hours=self.hours,
            minutes=self.minutes, seconds=self.seconds
        )

    def __str__(self):
        return self.title

# Wishlist
from django.db import models
from django.contrib.auth.models import User
from core.models import FeaturedProduct  # Update this to your actual product model

class WishItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FeaturedProduct, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
