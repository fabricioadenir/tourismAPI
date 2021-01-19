from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
from tourism.settings.base import BASE_DIR
from pathlib import Path

env_path = Path(BASE_DIR) / 'environment/tourism.env'
load_dotenv(dotenv_path=env_path)


class Command(BaseCommand):
    help = "Creates an admin user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument('--username', help="Admin's username")
        parser.add_argument('--email', help="Admin's email")
        parser.add_argument('--password', help="Admin's password")
        parser.add_argument(
            '--noinput', '--no-input', action='store_false', dest='interactive',
        )

    def handle(self, *args, **options):
        User = get_user_model()
        user = os.environ.get('DJANGO_SUPERUSER_USERNAME', options['username'])
        pwd = os.environ.get('DJANGO_SUPERUSER_EMAIL', options['email'])
        email = os.environ.get('DJANGO_SUPERUSER_PASSWORD', options['password'])
        if not User.objects.filter(username=user).exists():
            User.objects.create_superuser(username=user,
                                          email=email,
                                          password=pwd)
        else:
            print(f"That user '{user}' is already taken.")
