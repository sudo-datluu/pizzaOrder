from .customUser import CustomUser
from django.utils.translation import gettext_lazy as _
from .role import Role
from django.db.models import CharField

class Admin(CustomUser):
    class Meta:
        db_table = 'admin'
        verbose_name = _('Admin')
        verbose_name_plural = _('Admins')
