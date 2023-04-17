from django.utils.translation import gettext_lazy as _
from django.db import models

class Roster(models.Model):
    class WeekDay(models.TextChoices):
        MONDAY = 'MON', _('')
        TUESDAY = 'TUE', _('')
        WEDNESDAY = 'WED', _('')
        THURSDAY = 'THU', _('')
        FRIDAY = 'FRI', _('')
        SATURDAY = 'SAT', _('')
        SUNDAY = 'SUN', _('')
    weekday = models.CharField(
        max_length=3,
        choices=WeekDay.choices
    )
    def get_weekday(self) -> WeekDay:
        return self.WeekDay[self.weekday]
    start = models.TimeField()
    end = models.TimeField()
    noStaffs = models.IntegerField()

    class Meta:
        db_table = 'roster'
        verbose_name = _('Roster')
        verbose_name_plural = _('Rosters')
        constraints = [
            models.CheckConstraint(
                check=models.Q(end__gt=models.F('start')),
                name='check_time'
            )
        ]