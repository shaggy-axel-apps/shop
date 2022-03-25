from django.shortcuts import render

from mainapp.models import Product, ProductCategory

def index(request):
    return render(request, 'index.html')


def products(request):

    data = {
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    }
    return render(request, 'products.html', data)


def contacts(request):
    return render(request, 'contacts.html')
