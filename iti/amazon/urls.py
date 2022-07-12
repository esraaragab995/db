from django.urls import path
from amazon.views import homepage, contactus,aboutus,myproducts

urlpatterns = [
    path('home',homepage, name="homepage"),
    path('contactus',contactus ,name="contactuspage"),
    path('aboutus',aboutus, name="aboutuspage"),
    path('products/',myproducts, name='productspage'),
]