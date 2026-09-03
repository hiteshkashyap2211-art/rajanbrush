from django.shortcuts import render
from .models import Product, Category

def index(views_request):
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(views_request, 'index.html', context)

from django.shortcuts import render

def contact_view(request):
    return render(request, 'contact.html') # सुनिश्चित करें कि contact.html आपके templates फ़ोल्डर में है