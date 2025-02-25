from django.shortcuts import render
from django.utils.timezone import now
from .models import DailyAccess

def index(request):
    return render(request, 'accounts/index.html')

def statistics(request):
    today = now().date()
    total_acessos = DailyAccess.objects.filter(data=today).count()

    return render(request, 'accounts/statistics.html', {'total_acessos': total_acessos})