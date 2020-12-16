from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = decouple.config("DEBUG", default=1, cast=bool)

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}