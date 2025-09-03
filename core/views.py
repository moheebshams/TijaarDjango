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
def wishlist(request): return render(request, 'wishlist.html')
