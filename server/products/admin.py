from django.contrib import admin
from .models import Product, ProductReview,ProductStore


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductReviewInline]
    list_display = ("name","description","category")

class ProductStoreAdmin(admin.ModelAdmin):
    list_display = ("name","description")
    filter_horizontal = ("products",)


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductStore,ProductStoreAdmin)
