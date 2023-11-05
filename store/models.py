from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from category.models import School
from settings.models import Size


status_choices = (
    ('Published', 'Published'),
    ('Draft', 'Draft'),
)


class Product(models.Model):
    category = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=200, unique=True)
    description = RichTextUploadingField(_('Description'), blank=True)
    short_description = RichTextUploadingField(_('Short Description'), blank=True)
    images = models.ImageField(_('Image'), upload_to='store/%Y/%m/%d/')
    is_available = models.BooleanField(_('Is Available'), default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name


class Style(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=100, null=True)
    status = models.CharField(_('Status'), max_length=20, choices=status_choices, default='Published', null=True)
    created = models.DateTimeField(_('Created Date'), auto_now_add=True, editable=False)
    modified = models.DateTimeField(_('Modified Date'), auto_now=True, editable=False)

    def __str__(self):
        return self.title


class Variation(models.Model):
    category = models.ForeignKey(School, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to product directly
    style = models.ForeignKey(Style, on_delete=models.SET_NULL, null=True, blank=True)  # Style is now optional
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.DecimalField(_('Regular Price'), max_digits=10, decimal_places=2)
    stock = models.IntegerField(_('Stock'), default=1)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product.title}-{self.size.title}'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(_('Image'), upload_to='store/%Y/%m/%d/', max_length=255)

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Product Gallery'
        verbose_name_plural = 'Product Gallery'