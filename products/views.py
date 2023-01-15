from django.shortcuts import render,HttpResponse
from products.models import Product

# Create your views here.

def main(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def product_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }
        return render(request, 'products/products.html', context = context)

def queen(request):
    if request.method =='GET':
        return HttpResponse("You are cool, if you would like to buy mc'queen")