.PHONY:
.SILENT:

run:
	python run.py

up:
	docker-compose up -d

down:
	docker-compose down

migrate-up:
	alembic upgrade head

migrate-down:
	alembic downgrade -1

revision:
	alembic revision --autogenerate

