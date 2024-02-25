from django.urls import path
from .views import (
    salesperson_list,
    delete_salesperson,
    customer_list,
    delete_customer,
    sale_list,
    delete_sale,
    automobile_list,
    delete_automobile,
)

urlpatterns = [
    path('salespeople/', salesperson_list, name='salesperson_list'),
    path('salespeople/<int:id>/', delete_salesperson, name='delete_salesperson'),
    path('customers/', customer_list, name='customer_list'),
    path('customers/<int:id>/', delete_customer, name='delete_customer'),
    path('automobiles/', automobile_list, name='automobiles_list'),
    path('automobiles/<int:id>/', delete_automobile, name='delete_automobile'),
    path('sales/', sale_list, name='sale_list'),
    path('sales/<int:id>/', delete_sale, name='delete_sale'),
]
