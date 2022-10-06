from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Account)
admin.site.register(Review)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "category"
    )
    list_display_links = ("user","name")
    readonly_fields = []
    search_fields = [
        "user",
        "name",
    ]

admin.site.register(Product, ProductAdmin)