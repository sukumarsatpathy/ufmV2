from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    first_name = models.CharField(_('Parent First Name'), max_length=50)
    last_name = models.CharField(_('Parent Last Name'), max_length=50)
    email = models.EmailField(_('Email'), max_length=100, unique=True)
    phone_number = models.CharField(_('Contact No'), max_length=50)
    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyAccountManager()

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Account'
        db_table = 'accounts-list'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


class ProfilePicture(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_picture = models.ImageField(_('Picture'), blank=True, upload_to='userprofile')

    class Meta:
        verbose_name = 'Profile Picture'
        verbose_name_plural = 'Profile Picture'
        db_table = 'profile-picture-list'

    def __str__(self):
        return self.user.first_name


class Address(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(_('Address 1'), blank=True, max_length=100)
    address_line_2 = models.CharField(_('Address 2'), blank=True, max_length=100)
    city = models.CharField(_('City'), blank=True, max_length=20)
    state = models.CharField(_('State'), blank=True, max_length=20)
    country = models.CharField(_('Country'), blank=True, max_length=20)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Address'
        db_table = 'address-list'

    def __str__(self):
        return self.user.first_name

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'