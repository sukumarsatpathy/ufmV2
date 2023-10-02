from django.contrib import admin
from django.utils.html import format_html
from .models import School


class SchoolAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html('<img src="{}" width="50" />'.format(obj.logo.url))
    thumbnail.short_description = 'Logo'
    list_display = (
        'id', 'thumbnail', 'type', 'name', 'sname', 'code', 'status', 'modified_date', 'created_date')
    list_display_links = ('type', 'name', 'sname', 'code')
    search_fields = ('type', 'name', 'sname', 'code')
    prepopulated_fields = {'slug': ('name',), }

    fieldsets = [
        ('Details', {
            'fields': ['type', 'name', 'slug', 'sname', 'code', 'logo']}),
        ('Status', {'fields': ['status', ]}),
        ('SEO Details', {'fields': ['meta_title', 'meta_description']}),
    ]


admin.site.register(School, SchoolAdmin)