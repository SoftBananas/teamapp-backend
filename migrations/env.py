import importlib
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from src.core.config import config

db = config.load().database

importlib.import_module("src.models")


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
alembic_config = context.config

section = alembic_config.config_ini_section
alembic_config.set_section_option(section, "DB_DRIVER", db.driver)
alembic_config.set_section_option(section, "DB_HOST", db.host)
alembic_config.set_section_option(section, "DB_PORT", db.port)
alembic_config.set_section_option(section, "DB_NAME", db.name)
alembic_config.set_section_option(section, "DB_PASSWORD", db.password)
alembic_config.set_section_option(section, "DB_USER", db.user)

# Interpret the core file for Python logging.
# This line sets up loggers basically.
if alembic_config.config_file_name is not None:
    fileConfig(alembic_config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = config.database.metadata

# other values from the core, defined by the needs of env.py,
# can be acquired:
# my_important_option = core.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = alembic_config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        alembic_config.get_section(alembic_config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
