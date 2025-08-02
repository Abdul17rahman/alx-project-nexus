from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This can be used to add additional fields or methods in the future.
    """
    pass

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
