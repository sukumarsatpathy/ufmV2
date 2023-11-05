from django.db import models
from django.utils.translation import gettext_lazy as _
from category.models import School
from accounts.models import Account


status_choices = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class ChildrenProfile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,  related_name="children_profiles", null=True)
    full_name = models.CharField(_('Children Full Name'), max_length=50, null=True)
    grade = models.CharField(_('Children Grade'), max_length=50, null=True)
    status = models.CharField(_('Status'), max_length=20, choices=status_choices, default='Published', null=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Children Profile'
        verbose_name_plural = 'Children Profile'
        db_table = 'profiles-children-profile-list'

    def __str__(self):
        return self.full_name


class ChildrenSchoolRel(models.Model):
    children = models.ForeignKey(ChildrenProfile, on_delete=models.CASCADE,  related_name="children_school_relation", null=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, verbose_name='Select School')
    scode = models.CharField(_('School Code'), max_length=10, null=True)
    status = models.CharField(_('Status'), max_length=20, choices=status_choices, default='Published', null=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Children School Relation'
        verbose_name_plural = 'Children School Relation'
        db_table = 'profiles-children-school-relation-list'

    def __str__(self):
        return f'{self.children.full_name} - {self.school.name}'