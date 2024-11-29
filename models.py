from django.db import models
#customer model
class Customer(models.Model):
    name = models.CharField(max_length=255, verbose_name="Customer Name")
    email = models.EmailField(unique=True, verbose_name="Customer Email")
    def __str__(self):
        return self.name

#order model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateField(auto_now_add=True, verbose_name="Order Date")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Amount")
    def __str__(self):
        return f"Order {self.id} - {self.customer.name}"
