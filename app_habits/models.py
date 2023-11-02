from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """ Сущность привычки """

    # Пользователь — создатель привычки.
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)

    # Место — место, в котором необходимо выполнять привычку.
    place = models.CharField(max_length=100, verbose_name='Место')
    # Время — время, когда необходимо выполнять привычку.
    time = models.TimeField(verbose_name='Время')
    # Действие — действие, которое, представляет из себя, привычка.
    action = models.TextField(verbose_name='Действие')
    # Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
    periodicity = models.PositiveIntegerField(default=1, verbose_name='Периодичность выполнения')
    # Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
    time_to_complete = models.IntegerField(verbose_name='Время на выполнение, в секундах')

    # Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
    pleasant_habit = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    # Связанная привычка — привычка, которая связана с другой привычкой,
    # важно указывать для полезных привычек, но не для приятных.
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная привычка', **NULLABLE)

    # Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
    reward = models.TextField(verbose_name='Вознаграждение за выполнение действия', **NULLABLE)

    # Признак публичности — привычки можно публиковать в общий доступ,
    # чтобы другие пользователи могли брать в пример чужие привычки.
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности привычки')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('pk',)
