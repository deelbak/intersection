from django.contrib import admin
from api.models import Product, District


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'district', 'name', 'description', 'rating', 'user')