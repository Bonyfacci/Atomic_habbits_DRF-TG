from django.db import models
from rest_framework.exceptions import ValidationError

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """ Сущность привычки """

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE,
                              help_text='Пользователь — создатель привычки.')

    place = models.CharField(max_length=100, verbose_name='Место',
                             help_text='Место — место, в котором необходимо выполнять привычку.')
    time = models.TimeField(verbose_name='Время',
                            help_text='Время — время, когда необходимо выполнять привычку.')
    action = models.TextField(verbose_name='Действие',
                              help_text='Действие — действие, которое, представляет из себя, привычка.')
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Периодичность выполнения',
                                              help_text='Периодичность (по умолчанию ежедневная) — '
                                                        'периодичность выполнения привычки для напоминания в днях.')
    time_to_complete = models.IntegerField(verbose_name='Время на выполнение, в секундах',
                                           help_text='Время на выполнение — время, которое предположительно '
                                                     'потратит пользователь на выполнение привычки.')

    pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки',
                                         help_text='Признак приятной привычки — привычка, '
                                                   'которую можно привязать к выполнению полезной привычки.')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE,
                                      help_text='Связанная привычка — привычка, которая связана с другой привычкой, '
                                                'важно указывать для полезных привычек, но не для приятных.')

    reward = models.TextField(verbose_name='Вознаграждение за выполнение действия', **NULLABLE,
                              help_text='Вознаграждение — чем пользователь должен себя вознаградить после выполнения.')

    is_public = models.BooleanField(default=False, verbose_name='Признак публичности привычки',
                                    help_text='Признак публичности — привычки можно публиковать в общий доступ, '
                                              'чтобы другие пользователи могли брать в пример чужие привычки.')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    def save(self, *args, **kwargs):
        """ Проверки выполнения привычки (должно быть не более 120 секунд) """
        if self.time_to_complete and self.time_to_complete > 120:
            raise ValidationError('Время выполнения привычки должно быть больше 0 и меньше 120 секунд!')
        return super().save(**kwargs)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('pk',)
