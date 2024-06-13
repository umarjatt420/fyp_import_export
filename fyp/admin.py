from django.contrib import admin
from .models import ProductCategory, ProductOwner, ShippingCompany, Product

# Register your models here.
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
	list_display=['category']

@admin.register(ProductOwner)
class ProductOwnerAdmin(admin.ModelAdmin):
	list_display=['owner_name', 'owner_contact','owner_email']

@admin.register(ShippingCompany)
class ShippingCompanyAdmin(admin.ModelAdmin):
	list_display=['company_name', 'company_contact', 'company_address']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display=['product_name', 'product_price', 'product_image','product_description', 'product_owner', 'product_category', 'product_shipping']