from django.db import models
from django.utils.translation import gettext_lazy as _


class WebSettings(models.Model):
    # Brand
    title = models.CharField(_('Brand Name'), max_length=255, null=True)
    slogan = models.CharField(_('Slogan'), max_length=255, null=True)

    # Logo
    logo_dark = models.ImageField(_('Logo Dark'), upload_to='settings/logo/%Y/%m/%d/')
    logo_light = models.ImageField(_('Logo Light'), upload_to='settings/logo/%Y/%m/%d/')
    favicon = models.FileField(_('Favicon'), upload_to='settings/favicon/%Y/%m/%d/')

    # Default User
    default_user = models.ImageField(_('Default User Image'), upload_to='settings/user/%Y/%m/%d/', null=True, blank=True)

    # Google reCaptcha V3
    public_key = models.CharField(_('Google reCaptcha Public Key'), max_length=255, null=True, blank=True)
    private_key = models.CharField(_('Google reCaptcha Private Key'), max_length=255, null=True, blank=True)

    # SEO
    meta_title = models.CharField(_('Meta Title'), max_length=60, null=True)
    meta_description = models.CharField(_('Meta Description'), max_length=158, null=True)
    meta_keywords = models.CharField(_('Meta Keywords'), max_length=255, null=True)

    created = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Web Setting'
        verbose_name_plural = 'Web Settings'
        db_table = 'settings-website'

    def __str__(self):
        return self.title