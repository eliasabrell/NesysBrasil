from django.db import models
import datetime

class Produtos(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Vendedor(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Vendas(models.Model):
    product = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    data = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.product.name