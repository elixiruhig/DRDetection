from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
import uuid
from datetime import datetime

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self,username,email,password=None):
        if not username:
            raise ValueError("Please enter an username")

        user = self.model(
            username = username
        )
        user.set_password(password)
        user.email = email
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password):
        user = self.create_user(username,email, password=password)
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=255, blank=False)
    username = models.CharField(max_length=255, blank=False, unique=True)
    user_id = models.UUIDField(unique=True, default=uuid.uuid4)
    email = models.EmailField(max_length=255, unique=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

class Report(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4)
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    age = models.PositiveIntegerField(blank=False, null=False)
    date = models.DateTimeField(default=datetime.now())
    photo = models.ImageField(upload_to='fundus_images',null=True)
