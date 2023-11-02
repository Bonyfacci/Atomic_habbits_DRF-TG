from django.urls import path

from app_habits.apps import AppHabitsConfig
from app_habits.views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = AppHabitsConfig.name


urlpatterns = [
    path('habit', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
