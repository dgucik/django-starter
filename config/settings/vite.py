from config.settings.django import BASE_DIR
from config.settings.env import settings

DJANGO_VITE = {
  "default": {
    "dev_mode": settings.DEBUG,
    "manifest_path": BASE_DIR / "assets" / "manifest.json",
  }
}