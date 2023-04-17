from django.db import models
from django.utils.translation import gettext_lazy as _

class Role(models.TextChoices):
    CUSTOMER = 'C', _('Customer')
    STAFF = 'S', _('Staff')
    ADMIN = 'A', _('Admin')
