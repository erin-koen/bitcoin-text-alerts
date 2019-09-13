from django.db import models
from django.contrib.auth.models import User


# create profile model to collect contact information about users
# use django user model to authenticate, profile to ... profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.PositiveSmallIntegerField(unique=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    alerts_lifetime = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
