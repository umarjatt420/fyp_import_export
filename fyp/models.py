from django.db import models

# Create your models here.

class ProductCategory(models.Model):
	category=models.CharField(max_length=120)
	def __str__(self):
		return self.category

class ProductOwner(models.Model):
	owner_name=models.CharField(max_length=120)
	owner_contact=models.CharField(max_length=120)
	owner_email=models.EmailField(null=True, blank=True)
	bank_name=models.CharField(max_length=120, null=True, blank=True)
	account_holder_name=models.CharField(max_length=120, null=True, blank=True)
	bank_account_number=models.CharField(max_length=120, null=True, blank=True)
	def __str__(self):
		return self.owner_name

class ShippingCompany(models.Model):
	company_name=models.CharField(max_length=120)
	company_contact=models.CharField(max_length=120)
	company_address=models.TextField()
	def __str__(self):
		return self.company_name

class Product(models.Model):
	product_name=models.CharField(max_length=120)
	product_price=models.CharField(max_length=120)
	product_description=models.TextField()
	product_image=models.FileField(null=True, blank=True)
	product_owner=models.ForeignKey(ProductOwner, on_delete=models.CASCADE)
	product_category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
	product_shipping=models.ForeignKey(ShippingCompany,on_delete=models.CASCADE)
	def __str__(self):
		return self.product_name
