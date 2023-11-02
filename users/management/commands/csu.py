from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            username='admin',
            telegram_username='admin',
            telegram_chat_id='12345',

            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()
