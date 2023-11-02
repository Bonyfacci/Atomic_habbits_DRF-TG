# Реализовано с помощью функции. Исключить одновременный выбор связанной привычки и указания вознаграждения.
# Реализовано в сущности. Время выполнения должно быть не больше 120 секунд.
# Реализовано с помощью функции. В связанные привычки могут попадать только привычки с признаком приятной привычки.
# Реализовано с помощью функции. У приятной привычки не может быть вознаграждения или связанной привычки.
# Реализовано с помощью класса. Нельзя выполнять привычку реже, чем 1 раз в 7 дней.
from rest_framework.exceptions import ValidationError


def choose_related_habit_or_reward(related_habit, reward):
    """ Исключения одновременного выбора связанной привычки и указания вознаграждения. """

    if related_habit and reward:
        raise ValidationError('Привычка должна быть либо со связанной привычкой, либо с награждением!')


def check_pleasant_habit_with_related_habit(related_habit):
    """ Проверки связанной привычки с признаком приятной привычки. """

    if related_habit and not related_habit.pleasant_habit:
        raise ValidationError('Связанная привычка должна быть приятной приятной!')


def check_no_reward_or_related_habit_for_pleasant_habit(data):
    """ Проверки приятной привычки на наличие вознаграждения или связанной привычки. """

    pleasant_habit = data.get('pleasant_habit')
    reward = data.get('reward')
    related_habit = data.get('related_habit')

    if pleasant_habit and (reward or related_habit):
        raise ValidationError('У приятной привычки не должно быть вознаграждения или связанной привычки!')


class PeriodicityHabitValidator:
    """ Проверки периодичности привычки на выполнение не реже 1 раза в 7 дней. """

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        periodicity = dict(value).get(self.field)
        if periodicity > 7 or periodicity == 0:
            raise ValidationError('Привычка должна выполняться не реже 1 раза в 7 дней!')
