.PHONY: migrate dev prod

migrate:
	uv run python manage.py makemigrations
	uv run python manage.py migrate

dev:
	npm run dev &
	uv run python manage.py runserver 0.0.0.0:8000

prod:
	docker compose --env-file .env up --build