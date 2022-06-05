from django.db import models

from utils.models import TimeStampZone

class Category(models.Model):
    title = models.CharField(max_length=45)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'


class Color(models.Model): 
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name

    class Meta: 
        db_table = 'colors'

class Product(models.Model): 
    name     = models.CharField(max_length=45)
    price    = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey('Category', on_delete = models.CASCADE,related_name='categories')
    colors   = models.ForeignKey('Color', on_delete=models.PROTECT ,related_name='colors')
    inventory = models.IntegerField()
    
    class Meta: 
        db_table = 'products'

class Image(TimeStampZone): 
    product_color = models.ForeignKey('ProductColor', on_delete=models.CASCADE)
    image_url     = models.CharField(max_length=3000)
    sequence      = models.IntegerField()

    class Meta: 
        db_table = 'images'

class ProductColor(TimeStampZone): 
    product   = models.ForeignKey('Product', on_delete=models.CASCADE)
    color     = models.ForeignKey('Color', on_delete=models.CASCADE)

    class Meta: 
        db_table = 'productcolors'