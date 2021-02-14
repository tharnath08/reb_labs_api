from django.db import models

# Create your models here.
class Categories(models.Model):
    'model class for categories'
    owner = models.ForeignKey('auth.User', related_name='category', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Products(models.Model):
    'model class for products'
    owner = models.ForeignKey('auth.User', related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="product")
    product_image = models.ImageField(default='null')
    price = models.IntegerField()
    discount_price = models.IntegerField()
    adding_quantity = models.IntegerField()
    updating_price = models.IntegerField()
    in_stock = models.BooleanField(default= True)

    def __str__(self):
        return self.name