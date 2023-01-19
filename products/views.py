
from django.shortcuts import render,HttpResponse
from products.models import Product, Comment

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

def product_detail_view(request,id):
    if request.method =='GET':
        product_obj = Product.objects.get(id=id)
        comments = Comment.objects.filter(post=product_obj)
        context={
            'product' : product_obj,
            'comments' : comments
        }
        return render(request, 'products/detail.html',context = context)