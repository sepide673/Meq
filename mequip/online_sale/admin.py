from django.contrib import admin
from online_sale.models import *

# Register your models here.
admin.site.register(User)
admin.site.regirster(Customer)
admin.site.regirster(Category)
admin.site.regirster(Brand)
admin.site.regirster(Order)
admin.site.regirster(OrderItem)
