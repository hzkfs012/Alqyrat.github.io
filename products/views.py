#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product
from datetime import datetime

def product_list(request):
    products = Product.objects.all()
    current_date = datetime.now().strftime("%B %d, %Y")
    #current_date_ar = datetime.now().strftime("%d %B، %Y") 
    return render(request, 'products/product_list.html', {
        'products': products,
        'current_date': current_date,
        #'current_date_ar': current_date_ar,
        })



