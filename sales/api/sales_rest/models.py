from django.db import models

class Salesperson(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100, unique=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

class AutomobileVO(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    sold = models.BooleanField(default=False)

class Sale(models.Model):
    automobile = models.ForeignKey(
        AutomobileVO,
        on_delete=models.CASCADE
    )
    salesperson = models.ForeignKey(
        Salesperson,
        on_delete=models.CASCADE
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
