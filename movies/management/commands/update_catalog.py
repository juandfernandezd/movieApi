from django.core.management.base import BaseCommand, CommandError
from movies.functions import get_movies


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            get_movies()
            message = "Movies updated successfully"
            self.stdout.write(self.style.SUCCESS(message))
        except:
            raise CommandError('Error on update movie catalog')

