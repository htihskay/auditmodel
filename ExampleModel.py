from django.db import models
from audit.models import AuditModel  # Assuming AuditModel is defined in audit.models

class Order(AuditModel):
    order_number = models.CharField(max_length=20, unique=True)
    customer_name = models.CharField(max_length=100)
    order_date = models.DateField()
    shipping_date = models.DateField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled')
    ])

    def __str__(self):
        return f"Order {self.order_number} for {self.customer_name}"

