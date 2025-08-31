from django.shortcuts import render

# Single source for all categories
CATEGORIES = [
    {'name': 'Kitchen', 'icon': 'fa-utensils', 'products': 42},
    {'name': 'Bedroom', 'icon': 'fa-bed', 'products': 28},
    {'name': 'Bathroom', 'icon': 'fa-bath', 'products': 35},
    {'name': 'Living Room', 'icon': 'fa-couch', 'products': 56},
    {'name': 'Garden', 'icon': 'fa-leaf', 'products': 24},
    {'name': 'Office', 'icon': 'fa-laptop', 'products': 19},
    {'name': 'Cleaning', 'icon': 'fa-broom', 'products': 31},
    {'name': 'Storage', 'icon': 'fa-box', 'products': 27},
    {'name': 'Decor', 'icon': 'fa-paint-brush', 'products': 48},
    {'name': 'Lighting', 'icon': 'fa-lightbulb', 'products': 22},
    {'name': 'Laundry', 'icon': 'fa-soap', 'products': 18},
    {'name': 'Dining', 'icon': 'fa-utensil-spoon', 'products': 33},
    {'name': 'Kids Room', 'icon': 'fa-child', 'products': 25},
    {'name': 'Pets', 'icon': 'fa-paw', 'products': 15},
    {'name': 'Garage', 'icon': 'fa-warehouse', 'products': 20},
    {'name': 'Balcony', 'icon': 'fa-chair', 'products': 12},
    {'name': 'Home Gym', 'icon': 'fa-dumbbell', 'products': 17},
    {'name': 'Entryway', 'icon': 'fa-door-open', 'products': 14},
    {'name': 'Outdoor Furniture', 'icon': 'fa-campground', 'products': 21},
    {'name': 'Smart Home', 'icon': 'fa-house-signal', 'products': 29},
]

# Views
def home(request):
    return render(request, 'index.html', {'categories': CATEGORIES[:10]})  # first 10 only

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
