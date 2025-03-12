from django.contrib import admin
from .models import Vendas, Produtos, Vendedor

admin.site.register(Vendas)
admin.site.register(Produtos)
admin.site.register(Vendedor)
