from .base import *
import decouple
import sys

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = decouple.config("DEBUG", default=1, cast=bool)

ALLOWED_HOSTS += ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': f"{BASE_DIR}/db.sqlite3",
    }
}


# Covers regular testing and django-coverage
if 'test' in sys.argv or 'test_coverage' in sys.argv:
    DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

SOUTH_TESTS_MIGRATE = False
