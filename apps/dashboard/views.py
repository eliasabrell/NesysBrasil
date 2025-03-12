from django.shortcuts import render
from .models import Vendas, Produtos, Vendedor
from django.http import JsonResponse
from django.db.models import Sum
from datetime import datetime

def index(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    return render(request, 'accounts/login.html')

def all_data(request):
    if request.user.is_authenticated:
        current_month = datetime.now().month
        data = sum(range(1, current_month + 1))
        data = data if data > 0 else 1
        data_json = {'data': data}
        return JsonResponse(data_json)
    return render(request, 'accounts/login.html')

def all_products(request):
    if request.user.is_authenticated:
        product = Vendas.objects.all().aggregate(Sum('product'))["product__sum"]
        return JsonResponse({'product': product})
    return render(request, 'accounts/login.html')

def all_quantity(request):
    if request.user.is_authenticated:
        quantity = Vendas.objects.all().aggregate(Sum('quantity'))["quantity__sum"]
        return JsonResponse({'quantity': quantity})
    return render(request, 'accounts/login.html')

def billing_report(request):
    if request.user.is_authenticated:
        x = Vendas.objects.all()
        months = ["Janeiro", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        data = []
        labels = []
        month = datetime.now().month + 1
        year = datetime.now().year
        for i in range(12):
            month -= 1
            if month == 0:
                month = 12
                year -= 1
            y = sum([i.quantity for i in x if i.data.month == month and i.data.year == year])
            labels.append(months[month-1])
            data.append(y)
        data_json={'labels': labels[::-1], 'data': data[::-1]}
        return JsonResponse(data_json)
    return render(request, 'accounts/login.html')

def products_report(request):
    if request.user.is_authenticated:
        products = Produtos.objects.all()
        labels = []
        data = []
        for product in products:
            orders = Vendas.objects.filter(product=product).aggregate(Sum('quantity'))
            if not orders['quantity__sum']:
                orders['quantity__sum'] = 0
            labels.append(product.name) 
            data.append(orders['quantity__sum'])

        x = list(zip(labels, data))
        x.sort(key=lambda x: x[1], reverse=True)
        x = list(zip(*x))
        return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})
    return render(request, 'accounts/login.html')

def top_sellers(request):
    if request.user.is_authenticated:
        sellers = Vendedor.objects.all()
        labels = []
        data = []
        for seller in sellers:
            orders = Vendas.objects.filter(seller=seller).aggregate(Sum('quantity'))
            if not orders['quantity__sum']:
                orders['quantity__sum'] = 0
            labels.append(seller.name) 
            data.append(orders['quantity__sum'])

        x = list(zip(labels, data))
        x.sort(key=lambda x: x[1], reverse=True)
        x = list(zip(*x))
        return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})
    return render(request, 'accounts/login.html')
