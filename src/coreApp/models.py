# ------------for custom auth manager----------
from django.contrib.auth.models import BaseUserManager
# ------------for custom auth model------------------
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.db import models
# ---------------------- custom auth login manager and models----------------------------

# -----------------------manager-----------------------------------


class MyUserManager(BaseUserManager):
    """
    A custom user manager to deal with emails as unique identifiers for auth
    instead of usernames. The default that's used is "UserManager"
    """
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


# --------------custom model------------------------
class User(AbstractUser):

    _client_status_list = (
            ('subscriber', 'Subscriber'),
            ('qualified', 'Qualified'),
            ('qual-lead', 'Qual-Lead'),
            ('lead', 'Lead'),
            ('applied', 'Applied'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('drop_out', 'Drop Out'),
            ('un_subscribed', 'Un-subscribed')
        )


    username = models.CharField(max_length=150, unique=False, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    client_status = models.CharField(max_length=50, null=True, blank=True, choices=_client_status_list)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    @property
    def full_name(self):
        return self.first_name+' '+self.last_name

    def get_short_name(self):
        return self.email
