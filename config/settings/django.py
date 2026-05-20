from pathlib import Path

from config.settings.env import settings

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = settings.SECRET_KEY

DEBUG = settings.DEBUG

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

INTERNAL_IPS = ["127.0.0.1", "::1"]

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

ASGI_APPLICATION = "config.asgi.application"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"