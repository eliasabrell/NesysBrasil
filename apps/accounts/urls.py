from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('accounts', views.index, name='index'),
    path('statistics', views.statistics, name='statistics'),
]