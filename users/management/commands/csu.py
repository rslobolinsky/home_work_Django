from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='romansl1313@yandex.ru',
            first_name='Roman',
            last_name='Slobolinsky',
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('RoMaN199')
        user.save()
