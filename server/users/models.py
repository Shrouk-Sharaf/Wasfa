from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, name, phone, password=None, is_admin=False):
        """
        Creates and saves a regular User with the given email, name, phone and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            is_admin=is_admin
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, password):
        user = self.create_user(
            email=email,
            name=name,
            phone=phone,
            password=password,
            is_admin=True
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)  
    is_staff = models.BooleanField(default=False) 

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return self.is_admin
