from django.contrib import admin
from .models import Product, Pizza, Staff, Admin, Customer

# Register your models here.
admin.site.register(Product)
admin.site.register(Pizza)
admin.site.register(Staff)
admin.site.register(Admin)
admin.site.register(Customer)