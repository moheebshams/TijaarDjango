from django.shortcuts import render
from .models import*
from django.utils.timezone import now


def home(request):
    return render(request, 'index.html', {
        'slides': Slide.objects.all(),
        'categories': Category.objects.all(),
                'featured_products': FeaturedProduct.objects.all(),
                'electronics_product': ElectronicsProduct.objects.all(),
                'home_decor_product': HomeDecorProduct.objects.all(),
                             'customers': Customer.objects.all(),
        'stats': Stat.objects.all(),
                                        'features': WhyFeature.objects.all(),
                                              'offer': Offer.objects.filter(start_time__lte=now()).last(),  




        })

def category(request):
    
    return render(request, 'category.html', {'categories': CATEGORIES[:10]})  # first 10 only

def categories(request):
    return render(request, 'categories.html', {'categories': CATEGORIES})  # all categories

# Other views remain the same
def header(request): return render(request, 'header.html')
def hero(request): return render(request, 'hero.html')
def featured(request): return render(request, 'featured.html')
def electronics(request): return render(request, 'electronics.html')
def decor(request): return render(request, 'decor.html')
def customer(request): return render(request, 'customer.html')
def why(request): return render(request, 'why.html')
def offer(request): return render(request, 'offer.html')
def footer(request): return render(request, 'footer.html')
def addToCart(request): return render(request, 'addToCart.html')
def form(request): return render(request, 'form.html')
def trackYourOrder(request): return render(request, 'trackYourOrder.html')
def products(request): return render(request, 'products.html')
def productDetail(request): return render(request, 'productDetail.html')


# Wishlist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from .models import WishItem
from core.models import FeaturedProduct
from django.views.decorators.http import require_POST

@login_required(login_url='form')
def wishlist(request):
    wishlist_items = WishItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {
        'wishlist_items': wishlist_items,
        'wishlist_count': wishlist_items.count(),
    })

@login_required
@require_POST
def toggle_wishlist(request, product_id):
    product = get_object_or_404(FeaturedProduct, id=product_id)
    wish_item, created = WishItem.objects.get_or_create(user=request.user, product=product)

    if not created:  # Already exists → Remove
        wish_item.delete()
        return JsonResponse({'status': 'removed', 'message': f"{product.name} removed from wishlist!"})
    else:  # Added
        return JsonResponse({'status': 'added', 'message': f"{product.name} added to wishlist!"})

@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(WishItem, id=item_id, user=request.user)
    product_name = item.product.name
    item.delete()
    messages.success(request, f"{product_name} removed from your wishlist!")
    return redirect('wishlist')
