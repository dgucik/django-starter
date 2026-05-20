from config.settings.django import BASE_DIR

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

STATICFILES_DIRS = [BASE_DIR / "assets"]
STATIC_ROOT = BASE_DIR / "staticfiles"
MEDIA_ROOT = BASE_DIR / "media"