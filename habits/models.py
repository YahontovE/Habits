from django.db import models

from users.models import User

NULLABLE = {
    'blank': True,
    'null': True
}


class Habit(models.Model):
    place = models.CharField(max_length=200, verbose_name='Место выполениня')
    time = models.TimeField(verbose_name='Время выполения')
    action = models.CharField(max_length=200, verbose_name='активность в пирвычке')
    is_pleasnt = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    linked = models.ForeignKey('self', on_delete=models.CASCADE, **NULLABLE, verbose_name='связанная привычка')
    period = models.IntegerField(default=1, verbose_name='колличество выполнений в неделю')
    reward = models.CharField(max_length=150, verbose_name='награда за привычку')
    duration = models.IntegerField(verbose_name='время выполнения в секундах')
    is_public = models.BooleanField(verbose_name='признак публичности')

    last_sending = models.DateTimeField(verbose_name='дата последней отправки', **NULLABLE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='владелец', **NULLABLE)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
