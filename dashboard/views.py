from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request, 'dashboard/index.html')

@login_required
def staff(request):
    workers = User.objects.all()
    context= {
        'workers': workers,
    }
    return render(request, 'dashboard/staff.html', context)

def staff_detail(request,pk):
    return render(request, 'dashboard/staff_detail.html')

@login_required
def products(request):
    items = Product.objects.all()
    # items = Product.objects.raw('SELECT * FROM dashboard_product')

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    
    context={
        'items':  items,
        'form': form,
    }
    return render(request, 'dashboard/products.html', context)


def product_delete(request,pk):
    item = Product.objects.get(id=pk)
    if request.method== 'POST':
        item.delete()
        return redirect('dashboard-products')
    return render(request, 'dashboard/product_delete.html')

def product_update(request,pk):
    item = Product.objects.get(id=pk)
    if request.method== 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form= ProductForm(instance=item)
    context={
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required
def order(request):
    return render(request, 'dashboard/orders.html')

