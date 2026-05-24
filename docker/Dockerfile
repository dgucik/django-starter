# ── Stage 1: frontend build ───────────────────────────────────────────────────
FROM node:22-alpine AS frontend
WORKDIR /app
COPY package.json package-lock.json* ./
RUN npm ci
COPY vite.config.js .
COPY static/ ./static/
COPY pages/templates/ ./pages/templates/
RUN npm run build

# ── Stage 2: python dependencies ─────────────────────────────────────────────
FROM python:3.13-alpine AS deps
WORKDIR /app
RUN pip install uv
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-install-project

# ── Stage 3: runtime ─────────────────────────────────────────────────────────
FROM python:3.13-alpine AS runtime

RUN apk add --no-cache libpq

RUN addgroup -S app && adduser -S -G app app
WORKDIR /app

COPY --from=deps --chown=app:app /app/.venv /app/.venv
COPY --chown=app:app . .
COPY --from=frontend --chown=app:app /app/assets ./assets

ENV PATH="/app/.venv/bin:$PATH" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN mkdir -p /app/staticfiles /app/media && chown app:app /app/staticfiles /app/media

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

USER app
EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]
