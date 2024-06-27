from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from base.models import Page
from order.models import OrderBracelet
from order.service import order_service
from shop.models import Category, Product, Bracelet


def categories(request):
    categories = Category.objects.filter()
    page = get_object_or_404(Page, slug='categories')
    context = {
        "categories": categories,
        "page": page,
    }
    return render(request, "categories.html", context=context)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()

    p = Paginator(products, 12)
    page_num = request.GET.get('page', 1)
    page = p.page(page_num)

    context = {
        "category": category,
        "page": page,
    }
    return render(request, 'products.html', context=context)


def product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    recommend_products = Product.objects.filter().order_by('?')[:4]

    context = {
        "product": product,
        "recommend_products": recommend_products,
    }
    return render(request, 'product.html', context=context)


def constructor(request):
    category_constructor = Category.objects.filter(is_constructor=True)[0]
    page = get_object_or_404(Page, slug='constructor')
    context = {
        "products": category_constructor.products.all(),
        "page": page,
    }
    return render(request, 'constructor.html', context=context)


def constructor_save(request):
    selected_items = request.POST.get('selected_items').split(',')

    bracelet = Bracelet()
    bracelet.save()
    for item in selected_items:
        product = Product.objects.get(id=item)
        bracelet.products.add(product)

    order = order_service.get_order(request)
    brac = OrderBracelet(
        order=order,
        bracelet=bracelet)
    brac.save()
    return redirect('order')
