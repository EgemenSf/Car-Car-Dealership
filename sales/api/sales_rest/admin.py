from django.contrib import admin
from .models import Salesperson, Customer, AutomobileVO, Sale

class SalespersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'employee_id', 'id')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address', 'phone_number')

class AutomobileVOAdmin(admin.ModelAdmin):
    list_display = ('vin', 'sold', 'id')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('automobile', 'salesperson', 'customer', 'price', 'id')

admin.site.register(Salesperson, SalespersonAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(AutomobileVO, AutomobileVOAdmin)
admin.site.register(Sale, SaleAdmin)
