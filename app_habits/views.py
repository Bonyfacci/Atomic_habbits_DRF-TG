from rest_framework import generics

from app_habits.models import Habit
from app_habits.paginators import HabitPaginator
from app_habits.serializers import HabitSerializer


class HabitListAPIView(generics.ListAPIView):
    """ Контроллер просмотра всех привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitCreateAPIView(generics.CreateAPIView):
    """ Контроллер создания привычки """

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Контроллер просмотра привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Контроллер редактирования привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Контроллер удаления привычки """

    queryset = Habit.objects.all()
