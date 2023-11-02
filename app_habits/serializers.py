from rest_framework import serializers

from app_habits.models import Habit


class HabitSerializer(serializers.ModelSerializer):
    """ Сериализатор привычки """

    class Meta:
        model = Habit
        fields = '__all__'