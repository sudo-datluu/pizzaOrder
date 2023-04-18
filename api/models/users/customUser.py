from .role import Role
from django.contrib.auth.models import User
from django.db import models

class CustomUser(User):
    role = models.CharField(
        max_length=1,
        choices=Role.choices
    )

    def set_role(self, roleNotation: chr):
        roleDict = {
            'C': Role.CUSTOMER,
            'S': Role.STAFF,
            'A': Role.ADMIN
        }
        role = roleDict.get(roleNotation)
        if role:
            self.role = role
            self.save()
        