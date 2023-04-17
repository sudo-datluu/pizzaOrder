from .users import Customer
from .product import Product
from django.db import models
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', on_delete=models.CASCADE)
    totalPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at',] 
        db_table = 'order'
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
    
    def __str__(self):
        return '%s' % self.id

class OrderLine(models.Model):
    class Meta:
        db_table = 'order_line'
        verbose_name = _('OrderLine')
        verbose_name_plural = _('OrderLines')

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id