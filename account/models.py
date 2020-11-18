from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from account.managers import UserManager

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class User(AbstractUser):
    username = None
    role = models.CharField(max_length=12, error_messages={
        'required': "Role must be provided"
    })
    gender = models.CharField(max_length=10, blank=True, null=True, default="")
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __unicode__(self):
        return self.email

    objects = UserManager()
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='media')
 
    def __str__(self):
        return self.user.first_name

    # def user_name(self):
    #     return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    