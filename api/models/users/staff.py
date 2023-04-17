from django.contrib.auth.models import User
from .role import Role
from api.models.roster import Roster
from django.db import models
from django.utils.translation import gettext_lazy as _

class Staff(User):
    class Meta:
        db_table = 'staff'
        verbose_name = _('Staff')
        verbose_name_plural = _('Staffs')

    role = Role.STAFF
    rosters = models.ManyToManyField(Roster)

    