from .customUser import CustomUser
from .role import Role
from api.models.roster import Roster
from django.db import models
from django.utils.translation import gettext_lazy as _

class Staff(CustomUser):
    class Meta:
        db_table = 'staff'
        verbose_name = _('Staff')
        verbose_name_plural = _('Staffs')

    rosters = models.ManyToManyField(Roster, blank=True)