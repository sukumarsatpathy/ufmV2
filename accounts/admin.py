from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, ProfilePicture, Address


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()

    fieldsets = [
        ('Login Details', {'fields': ['email', 'password']}),
        ('Parent Details', {'fields': ['first_name', 'last_name', 'phone_number']}),
        ('Permission Details', {'fields': ['is_admin', 'is_staff', 'is_active', 'is_superuser']}),
    ]


admin.site.register(Account, AccountAdmin)
admin.site.register(ProfilePicture)
admin.site.register(Address)