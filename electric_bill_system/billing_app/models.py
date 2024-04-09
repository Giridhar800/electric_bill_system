# billing/models.py

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # Add other customer-related fields as needed

    def __str__(self):
        return self.name

class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    # Add other bill-related fields as needed

    def __str__(self):
        return f"{self.customer.name} - {self.date}"

