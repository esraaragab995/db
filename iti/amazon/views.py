from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
    
products = [
    {
        "id":1,
        "image":"pexels1.jpg",
        "title": "image1",
        "details":"image details",
    },

    {
        "id":2,
        "image":"pexels1.jpg",
        "title": "image2",
        "details":"image details",
    },
    {
        "id":3,
        "image":"pexels1.jpg",
        "title": "image3",
        "details":"image details",
    },
    {
        "id":4,
        "image":"pexels1.jpg",
        "title": "image4",
        "details":"image details",
    },
    {
        "id":5,
        "image":"pexels1.jpg",
        "title": "image5",
        "details":"image details",
    },

    {
        "id":6,
        "image":"pexels1.jpg",
        "title": "image6",
        "details":"image details",
    },
]

def homepage(request):
    return render(request,'amazon/homepage.html')

def contactus(request):
    return render(request, 'amazon/contactus.html')

def aboutus(request):
    return render(request, 'amazon/aboutus.html')

def myproducts(request):
    return render(request,'amazon/products.html' ,context={'products':products})