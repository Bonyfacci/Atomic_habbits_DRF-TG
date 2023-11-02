from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'telegram_username', 'telegram_chat_id', 'is_staff', 'is_superuser')
    list_filter = ('is_superuser', 'is_staff', 'is_active')
    search_fields = ('telegram_username', 'telegram_chat_id')
