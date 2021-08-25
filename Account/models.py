from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from django.core import validators
from django.utils.safestring import mark_safe
from django.contrib.sessions.models import Session
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from tools.slug_generator import slugify

from django.contrib.auth.models import UserManager
class AccountManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)



# Customize User model
class User(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.
    First name, last name, date of birth and email are required. Other fields are optional.
    """
    username = models.CharField('Username', max_length=100,
                                validators=[
                                    validators.RegexValidator(r'^[\w.@+-]+$', 'Please enter valid username', )
                                ], blank=True)
    email = models.EmailField('Email address', max_length=255, unique=True, db_index=True)    
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    fisrt_name = models.CharField('name',max_length=50)
    last_surname = models.CharField('surname' , max_length=50)

    
    
    is_staff = models.BooleanField('staff status', default=False,
                                   help_text='Designates whether the user can log into this admin site.')
    is_active = models.BooleanField('active', default=True,
                                    help_text='Designates whether this user should be treated as active. '
                                              'Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('Date joined', default=timezone.now)
    # legacy fields
    old_psw_hash = models.CharField(blank=True, null=True, max_length=300)
    # slug for detail page
    slug = models.SlugField(max_length=255, null=True, blank=True)
    """
        Important non-field stuff
    """
    objects = AccountManager()
    REQUIRED_FIELDS = []
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        self.slug = slugify(str(self.date_joined.timestamp()))
        super(User, self).save(*args, **kwargs)

    def get_avatar(self):
        if self.image:
            return self.image.url
        return 'https://cdt.org/files/2015/10/2015-10-06-FB-person.png'

    @property
    def fullname(self):
        return self.name + self.surname

    