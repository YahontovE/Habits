from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {
    'blank': True,
    'null': True
}


class User(AbstractUser):
    user_id = models.PositiveIntegerField(unique=True, verbose_name='tg id', blank=True, null=True)
