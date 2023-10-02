from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


wear_type = (
    ('School Wear', 'School Wear'),
    ('Sports Wear', 'Sports Wear'),
    ('Spirit Wear', 'Spirit Wear'),
)


class School(models.Model):
    type = models.CharField(_('Wear Type'), max_length=11, choices=wear_type, default='School Wear')
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(_('Slug'), max_length=100, unique=True)
    sname = models.CharField(_('Short Name'), max_length=250, unique=True, null=True, help_text='Khalsa Community School: KCS')
    code = models.CharField(_('Code'), max_length=50, unique=True, null=True, help_text='Ex: KCS-01 / KCS01')
    logo = models.ImageField(_('Logo'), upload_to='category/logos/%Y/%m/%d/', null=True, blank=True, help_text='Size (in px): 300x300')
    status = models.BooleanField(_('Status'), default=True)
    created_date = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified_date = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)
    # SEO
    meta_title = models.CharField(_('Title'), max_length=70, blank=True)
    meta_description = models.TextField(_('Description'), max_length=160, blank=True)

    class Meta:
        verbose_name = 'School'
        verbose_name_plural = 'School'
        db_table = 'category-school-list'

    def __str__(self):
        return self.name

    def _generate_unique_slug(self):
        """
        Generate a unique slug for the Job model.
        """
        slug = original_slug = slugify(self.role)
        count = 1
        while School.objects.filter(slug=slug).exclude(id=self.id).exists():
            slug = "{}-{}".format(original_slug, count)
            count += 1
        return slug

    def save(self, *args, **kwargs):
        # Check if slug needs to be auto-generated or if the title has changed.
        if not self.slug or (self.id and School.objects.get(id=self.id).role != self.role):
            self.slug = self._generate_unique_slug()
        super(School, self).save(*args, **kwargs)