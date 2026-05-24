# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Development (run concurrently)
make dev                        # starts both Vite dev server and Django on port 8000

# Database
make migrate                    # runs makemigrations then migrate

# Individual servers
uv run python manage.py runserver 0.0.0.0:8000
npm run dev                     # Vite + Tailwind hot reload

# Frontend build (production)
npm run build

# Tests
uv run python manage.py test
uv run pytest                   # alternative with pytest

# Packages
uv add <package>                # add Python dependency
uv sync                         # install all dependencies
```

## Architecture

**Project layout:**
- `config/` — Django project package (urls, wsgi, asgi, settings/)
- `pages/` — root-level app handling all user-facing pages; templates live here
- `apps/users/` — custom `User` model (extends `AbstractUser`); `AUTH_USER_MODEL = "users.User"`
- `core/` — shared abstractions: `BaseModel` (adds `created_at`/`updated_at`), `BaseAppException`

**Settings are split** across `config/settings/` into per-concern modules (`django.py`, `database.py`, `auth.py`, `vite.py`, `unfold.py`, etc.). Environment is loaded via Pydantic settings in `env.py`. Copy `.env.example` to `.env` to configure locally.

**Database:** defaults to SQLite; set `DATABASE_ENGINE=postgresql` plus `POSTGRES_*` vars (or use `docker-compose up` for a local PostgreSQL 18 instance).

**Frontend stack:** Vite 8 + Tailwind CSS 4 + DaisyUI + HTMX 2. JavaScript entry is `static/js/main.js`; compiled output goes to `assets/`. Templates use `{% vite_hmr_client %}` / `{% vite_asset %}` tags. HTMX boost is enabled on `<body>` in `base.html`.

**Admin:** Django Unfold replaces the default admin dashboard (dark mode enabled).

**New apps** should extend `BaseModel` for consistent timestamps and be registered under `INSTALLED_APPS` in `config/settings/installed_apps.py`.
