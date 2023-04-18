from .customUser import CustomUser
from django.db.models import IntegerField, CharField
from .role import Role
from django.utils.translation import gettext_lazy as _

class Customer(CustomUser):
    class Meta:
        db_table = 'customer'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    loyalPoints = IntegerField(default=0)