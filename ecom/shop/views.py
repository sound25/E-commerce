from django.core import paginator
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Products
# Create your views here.
def index(request):
    product_objects=Products.objects.all()

    #search code
    item_name=request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects=Products.objects.filter(title__icontains=item_name)

    #Paginator code
    paginator=Paginator(product_objects,2)
    page=request.GET.get('page')
    product_objects=paginator.get_page(page)

    return render(request, 'shop/index.html',{'product_objects':product_objects})



