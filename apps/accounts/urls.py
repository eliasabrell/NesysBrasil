from django.urls import path
from . views import index
from . views import statistics

app_name = 'accounts'
urlpatterns = [
    path('accounts', index, name='index'),
    path('statistics', statistics, name='statistics'),
]