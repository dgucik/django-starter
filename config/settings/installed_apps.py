DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "debug_toolbar",
    "django_vite",
    "widget_tweaks",
]

LOCAL_APPS = [
    "apps.core",
    "apps.pages",
    "apps.users",
]

INSTALLED_APPS = (
    DJANGO_APPS 
    + THIRD_PARTY_APPS
    + LOCAL_APPS
)