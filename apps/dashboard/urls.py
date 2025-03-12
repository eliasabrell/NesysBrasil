from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_quantity/', views.all_quantity, name='all_quantity'),
    path('all_data/', views.all_data, name='all_data'),
    path('all_products/', views.all_products, name='all_products'),
    path('billing_report/', views.billing_report, name='billing_report'),
    path('products_report/', views.products_report, name='products_report'),
    path('top_sellers/', views.top_sellers, name='top_sellers'),
]