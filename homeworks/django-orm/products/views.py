from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .models import Category


def add_product(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "products/add.html")
        else:
            product = Product()
            product.title = request.POST.get("title")
            product.description = request.POST.get("description")
            product.category = request.POST.get("category")
            product.user = request.user
            product.save()
            return redirect("/")
    else:
        return redirect("/")


def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, "products/details.html", {"product": product})


def show_products(request):
    category = request.GET.get("category")

    if category == None:
        products = Product.objects.order_by('-title')
    else:
        products = Product.objects.filter(category__category_name=category)

    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories
    }

    return render(request, "products/show.html", context)