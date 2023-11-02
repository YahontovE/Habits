import datetime

import requests
from django.utils import timezone


def get_message(habit):
    """Создание напоминания пользователю"""
    if habit.reward:
        reward = habit.reward
    elif habit.linked:
        reward = habit.linked.action
    else:
        reward = 'Отсутствует'

    return (f'Уведомление о выполнении привычки! '
            f'\nВыполнить: {habit.action}. '
            f'\nМесто: {habit.place}. '
            f'\nВремя: {habit.time}. '
            f'\nВремя на выполнение: {habit.duration} секунд. '
            f'\nНаграда: {reward}.')


def send_tg_message(habit, full_url):
    """Проверка на наличие логов, их запись и отправка сообщения пользователю"""
    now = timezone.now()

    if habit.last_sending:
        if habit.last_sending <= now - datetime.timedelta(days=habit.period):
            requests.get(full_url)
            habit.last_sending = timezone.now()
            habit.save()

    else:
        if habit.time <= now.time():
            requests.get(full_url)
            habit.last_sending = timezone.now()
            habit.save()
