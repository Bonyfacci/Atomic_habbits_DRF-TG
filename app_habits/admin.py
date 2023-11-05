from django.contrib import admin

from app_habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'owner',
                    'place', 'time', 'action', 'periodicity', 'time_to_complete',
                    'pleasant_habit', 'related_habit',
                    'reward',
                    'is_public',
                    'last_send',)
    list_filter = ('owner', 'place', 'is_public', 'pleasant_habit')
    search_fields = ('owner', 'place', 'action', 'periodicity', 'reward')
