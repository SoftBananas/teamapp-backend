.PHONY:
.SILENT:


# Standard running application
run:
	python run.py

# Build docker image
build:
	docker-compose build

# Start docker containers
up:
	docker-compose up -d

# Stop docker containers
down:
	docker-compose down

# Migrate data to database
migrate-up:
	alembic upgrade head

# Rollback migrations in database
migrate-down:
	alembic downgrade -1

# Generate alembic revision
revision:
	alembic revision --autogenerate

