from config.settings.env import settings, DatabaseEngine
from config.settings.django import BASE_DIR

if settings.DATABASE_ENGINE == DatabaseEngine.SQLITE:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

elif settings.DATABASE_ENGINE == DatabaseEngine.POSTGRESQL:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": settings.POSTGRES_DB,
            "USER": settings.POSTGRES_USER,
            "PASSWORD": settings.POSTGRES_PASSWORD,
            "HOST": settings.POSTGRES_HOST,
            "PORT": settings.POSTGRES_PORT,
        }
    }

else:
    raise ValueError(f"Unsupported database engine: {settings.DATABASE_ENGINE}")