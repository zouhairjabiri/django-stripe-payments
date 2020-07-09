from django.db import models

# Create your models here.

class Product(models.Model):
	product_name = models.CharField(max_length=150)
	product_type = models.CharField(max_length=25)
	product_description = models.TextField()
	product_price = models.IntegerField()