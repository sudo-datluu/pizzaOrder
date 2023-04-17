from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .role import Role

class Admin(User):
    class Meta:
        db_table = 'admin'
        verbose_name = _('Admin')
        verbose_name_plural = _('Admins')

    role = Role.ADMIN

