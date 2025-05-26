from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class User(AbstractUser):
    """Class for all users"""

    def save(self, *args, **kwargs):
        if self.email:
            if self.__class__.objects.filter(email=self.email).exclude(pk=self.pk).exists():
                raise ValidationError("This email is already associated to another user.")
        super().save(*args, **kwargs)