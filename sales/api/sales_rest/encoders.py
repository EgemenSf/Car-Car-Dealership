from common.json import ModelEncoder
from decimal import Decimal
from .models import AutomobileVO, Sale, Salesperson, Customer

class AutomobileVOEncoder(ModelEncoder):
    model = AutomobileVO
    properties = [
        "vin",
        "sold",
        "id",
    ]

class SalespersonEncoder(ModelEncoder):
    model = Salesperson
    properties = [
        "first_name",
        "last_name",
        "employee_id",
        "id",
    ]

class CustomerEncoder(ModelEncoder):
    model = Customer
    properties = [
        "first_name",
        "last_name",
        "address",
        "phone_number",
        "id"
    ]

class SaleEncoder(ModelEncoder):
    model = Sale
    properties = [
        "id",
        "automobile",
        "salesperson",
        "customer",
        "price",

    ]
    encoders = {
        "automobile": AutomobileVOEncoder(),
        "salesperson": SalespersonEncoder(),
        "customer": CustomerEncoder(),
    }
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, Sale):
            return {
                "id": obj.id,
                "automobile": AutomobileVOEncoder().default(obj.automobile),
                "salesperson": SalespersonEncoder().default(obj.salesperson),
                "customer": CustomerEncoder().default(obj.customer),
                "price": float(obj.price)
            }
        return super().default(obj)
