from django.shortcuts import render
from .models import Order
from django.http import JsonResponse
from django.db.models import Sum

def index(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/index.html')
    return render(request, 'accounts/login.html')

def all_orders(request):
    All = Order.objects.all().aggregate(Sum('quantity'))["quantity__sum"]
    if request.method == 'GET':
        return JsonResponse({'Total': All})