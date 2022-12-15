from django.contrib.auth.models import User
from django.db import models
from store.models import Product


# Create your models here.

class Order(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f"Order {self.pk}"

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.orderitem_set.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.pk}"

    def get_cost(self):
        return self.price * self.quantity
