from django.contrib.auth.models import User
from django.db.models import IntegerField
from .role import Role
from django.utils.translation import gettext_lazy as _

class Customer(User):
    class Meta:
        db_table = 'customer'
        verbose_name = _('Customer')
        verbose_name_plural = _('Customers')

    role = Role.CUSTOMER
    loyalPoints = IntegerField(default=0)