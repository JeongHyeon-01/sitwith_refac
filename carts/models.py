from django.db import models
from utils.models import TimeStampZone

class Cart(TimeStampZone):
    user_info     = models.ForeignKey('users.user', on_delete=models.CASCADE, related_name='users')
    product_info  = models.ForeignKey('products.product', on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    
    def total_price(self):
        return self.quantity * self.product_info.price


    class Meta:
        db_table = 'carts'