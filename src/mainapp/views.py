from typing import NamedTuple
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

class Product(NamedTuple):
    name: str
    price: int

def products(request):
    product_1, product_2 = Product(name="Monitor", price="500"), Product(name="Keyboard", price="1000")
    data = {
        "products": [
            product_1, product_2
        ]
    }
    return render(request, 'products.html', data)


def contacts(request):
    return render(request, 'contacts.html')
