from cities_light.models import City
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from faker import Faker

from ad.models import Ad


class Command(BaseCommand):
    DESCRIPTION_SIZE = 2000
    TITLE_SIZE = 100

    help = "Add random ads"

    def add_arguments(self, parser):
        parser.add_argument('--user', help='username (default: last user)')
        parser.add_argument('--count', help='ad count (default: 40)', type=int, default=40)
        super().add_arguments(parser)

    def handle(self, *args, **options):
        fake = Faker()

        username = options.get('username')
        ad_count = options.get('count')
        usermodel = get_user_model()
        if username is None:
            user = usermodel.objects.last()
        else:
            try:
                user = usermodel.objects.get(username=username)
            except ObjectDoesNotExist:
                self.stderr = 'user does not exist'
                return

        for i in range(ad_count):
            Ad.objects.create(
                title=fake.text(self.TITLE_SIZE),
                description=fake.text(self.DESCRIPTION_SIZE),
                user=user,
                city=City.objects.order_by('?').first()
            )
            self.stdout = f'{ad_count} ads add'
