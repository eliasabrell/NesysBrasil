from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.utils.timezone import now
from .models import DailyAccess

def signup(request):
    if request.method == 'GET':
        return render (request, 'accounts/signup.html')
    else :
        username = request.POST.get('username')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Esse usuario ja existe!')
        
        user = User.objects.create_user(username=username, last_name=last_name, email=email, password=password)
        user.save()

        return render(request, 'accounts/index.html')


def login(request):
    if request.method == 'GET':
        return render (request, 'accounts/login.html')
    else :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=username, email=email, password=password)

        if user:
            login_django(request, user)
            return render(request, 'accounts/index.html')
        else:
            return HttpResponse('Usuário ou senha incorretos!')


def index(request):
    if request.user.is_authenticated:
        return render(request, 'accounts/index.html')
    return render(request, 'accounts/login.html')


def statistics(request):
    if request.user.is_authenticated:
        today = now().date()
        total_acessos = DailyAccess.objects.filter(data=today).count()
        return render(request, 'accounts/statistics.html', {'total_acessos': total_acessos})
    
    return render(request, 'accounts/login.html')
