from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY = {
        "J" : "JACKET",
        "S"  : "SHOE",
    }
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    image = models.ImageField(upload_to="uploads/")
    category = models.CharField(choices=CATEGORY,max_length=1)
    
    def __str__(self):
        return f'{self.name} and id {self.id}'

class ProductReview(models.Model):
    rating = models.IntegerField(default=0,)
    products = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="reviews")
    description = models.TextField(default="")

    def __str__(self):
        return f"{self.products.name} - {self.rating}"


class ProductStore(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    products = models.ManyToManyField(Product,related_name="stores")

    def __str__(self):
        return f"{self.name} - {self.description}"


