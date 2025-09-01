from django.shortcuts import render

# Hero slider
SLIDES = [
    {'image': 'images/slider/slide1.png'},
    {'image': 'images/slider/slide2.png'},
    {'image': 'images/slider/slide3.png'},
    {'image': 'images/slider/slide2.png'},
    {'image': 'images/slider/slide3.png'},
    {'image': 'images/slider/slide1.png'},
]

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

# Featured Products
FEATURED_PRODUCTS = [
    {
        'name': 'Modern Lamp',
        'image': 'images/featured/lamp.png',
        'price': '$49',
        'old_price': '$69',
        'discount': 30,
        'badge': 'New',
        'rating': 4,
        'reviews_count': 12
    },
    {
        'name': 'Wooden Chair',
        'image': 'images/featured/chair.png',
        'price': '$89',
        'old_price': '$120',
        'discount': 25,
        'badge': 'Hot',
        'rating': 5,
        'reviews_count': 34
    },
    {
        'name': 'Comfort Sofa',
        'image': 'images/featured/sofa.png',
        'price': '$299',
        'old_price': '$350',
        'discount': 15,
        'badge': 'Sale',
        'rating': 4,
        'reviews_count': 18
    },
    {
        'name': 'Kitchen Mixer',
        'image': 'images/featured/mixer.png',
        'price': '$59',
        'old_price': None,
        'discount': None,
        'badge': None,
        'rating': 3,
        'reviews_count': 5
    },
]

# Electronics Products
ELECTRONICS_PRODUCTS = [
    {
        'name': 'Gaming Console',
        'image': 'images/electronics/console.png', 
        'price': '$499',
        'old_price': '$549',
        'badge': 'New',
        'rating': 5,
        'reviews_count': 85,
        'description': 'Next-gen gaming console with stunning graphics and ultra-fast performance.'
    },
    {
        'name': 'Smart Watch',
        'image': 'images/electronics/watch.png',
        'price': '$199',
        'old_price': '$249',
        'badge': 'Hot',
        'rating': 4,
        'reviews_count': 40,
        'description': 'Track your fitness, notifications, and more with this stylish smart watch.'
    },
    {
        'name': 'Smart TV',
        'image': 'images/electronics/tv.png',
        'price': '$799',
        'old_price': '$899',
        'badge': 'Sale',
        'rating': 5,
        'reviews_count': 60,
        'description': '55-inch 4K Smart TV with HDR, streaming apps, and voice control.'
    },
]

# Home Decor Products
HOME_DECOR_PRODUCTS = [
    {
        'name': 'Decorative Vase',
        'image': 'images/decor/vases.png',
        'price': '$49',
        'old_price': '$69',
        'badge': 'New',
        'rating': 4,
        'reviews_count': 25,
        'description': 'Elegant decorative vase to enhance your living space.'
    },
    {
        'name': 'Wall Art Frame',
        'image': 'images/decor/art.png',
        'price': '$89',
        'old_price': '$109',
        'badge': 'Hot',
        'rating': 5,
        'reviews_count': 32,
        'description': 'Modern wall art frame to transform your room ambiance.'
    },
]

def home(request):
    return render(request, 'index.html', {
        'slides': SLIDES,
        'categories': CATEGORIES[:10],   # first 10 only
                'featured_products': FEATURED_PRODUCTS,
                        'electronics_products': ELECTRONICS_PRODUCTS,
                                'home_decor_products': HOME_DECOR_PRODUCTS


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
