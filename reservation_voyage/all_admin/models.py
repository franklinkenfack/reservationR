from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class AllAdminManager(BaseUserManager):
    def create_user(self, mail, password=None, **extra_fields):
        if not mail:
            raise ValueError('Le mail est obligatoire')
        user = self.model(mail=mail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mail, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(mail, password, **extra_fields)

class AllAdmin(AbstractBaseUser, PermissionsMixin):
    ADMIN_TYPES = [('SYS_ADMIN', 'Administrateur'), ('SUPER_ADMIN', 'Super Admin')]
    
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=150)
    mail = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    country_calling_code = models.CharField(max_length=5, blank=True, null=True)
    tel_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    localite = models.CharField(max_length=100, blank=True, null=True)
    admin_type = models.CharField(max_length=20, choices=ADMIN_TYPES, default='SYS_ADMIN')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['admin_name']
    
    objects = AllAdminManager()

    class Meta:
        verbose_name = 'AllAdmin'
        verbose_name_plural = 'AllAdmins'

    def __str__(self):
        return self.admin_name