from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import School
from accounts.models import Account


class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(_('Address 1'), blank=True, max_length=100)
    address_line_2 = models.CharField(_('Address 2'), blank=True, max_length=100)
    image = models.ImageField(_('Profile Picture'), blank=True, upload_to='userprofile/')
    city = models.CharField(_('City'), blank=True, max_length=20)
    state = models.CharField(_('State'), blank=True, max_length=20)
    country = models.CharField(_('Country'), blank=True, max_length=20)

    class Meta:
        verbose_name = 'Parent Profile'
        verbose_name_plural = 'Parent Profile'
        db_table = 'profiles-parent-list'

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'


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