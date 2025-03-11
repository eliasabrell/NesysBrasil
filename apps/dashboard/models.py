from django.db import models
import datetime

class Product(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name
    
class Seller(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.product.name