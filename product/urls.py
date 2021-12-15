from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about-us'),
    path('contact-us', views.contact_us, name='contact_us'),
    path('faq', views.faq, name='faq'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('order', views.order, name='order'),
    path('product-360-degree', views.product_360_degree, name='product-360-degree'),
    path('products', views.product, name='product'),
    path('shop', views.shop, name='shop'),
    path('store-listing', views.store_listing, name='store-listing'),
    path('wishlist', views.wishlist, name='wishlist'),
   
]