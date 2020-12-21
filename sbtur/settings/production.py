from .base import *
import decouple

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = decouple.config("DEBUG", default=0, cast=bool)

ALLOWED_HOSTS += ['seu_dns']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASE = decouple.config("DATABASE", default="sbtur")
DB_USER = decouple.config("DB_USER", default="sbtur_user")
DB_PWD = decouple.config("DB_PWD", default="sbtur_pwd")
DB_HOST = decouple.config("DB_HOST", default="localhost")
DB_PORT = decouple.config("DB_PORT", default=5432, cast=int)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DATABASE,
        'USER': DB_USER,
        'PASSWORD': DB_PWD,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]
