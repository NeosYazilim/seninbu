from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def about_us(request):
    return render(request,'about-us.html')
def contact_us(request):
    return render(request,'contact-us.html')
def faq(request):
    return render(request,'faq.html')
def login(request):
    return render(request,'login.html')
def cart(request):
    return render(request,'cart.html')
def checkout(request):
    return render(request,'checkout.html')
def order(request):
    return render(request,'order.html')
def product_360_degree(request):
    return render(request,'product-360-degree.html')
def product(request):
    return render(request,'product.html')
def shop(request):
    return render(request,'shop.html')
def store_listing(request):
    return render(request,'store-listing.html')
def wishlist(request):
    return render(request,'wishlist.html')
