from django.db import models
import products
from utils.models import TimeStampZone

class Cart(TimeStampZone):
    user_info     = models.ForeignKey('users.user', on_delete=models.CASCADE, related_name='users')
    product_info  = models.ForeignKey('products.product', on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    
    def single_price(self):
        return self.product_info.price

    def total_price(self):
        return self.quantity * self.product_info.price

    def __str__(self):
        return self.product_info.name
    
    class Meta:
        db_table = 'carts'