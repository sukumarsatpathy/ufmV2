from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import School
from accounts.models import Account


class ChildrenProfile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,  related_name="children_profiles", null=True)
    full_name = models.CharField(_('Children Full Name'), max_length=50, null=True)
    grade = models.CharField(_('Children Grade'), max_length=50, null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, verbose_name='Select School')
    scode = models.CharField(_('School Code'), max_length=10, null=True)

    class Meta:
        verbose_name = 'Children Profile'
        verbose_name_plural = 'Children Profile'
        db_table = 'profiles-children-profile-list'

    def __str__(self):
        return self.full_name