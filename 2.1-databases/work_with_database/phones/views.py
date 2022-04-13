from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort', 'id')
    if sorting and sorting in ['name', 'min_price', 'max_price']:
        if sorting == 'min_price':
            sorting = 'price'
        elif sorting == 'max_price':
            sorting = '-price'
    context = {'phones': Phone.objects.all().order_by(sorting)}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone': Phone.objects.get(slug=slug).__dict__}
    return render(request, template, context)
