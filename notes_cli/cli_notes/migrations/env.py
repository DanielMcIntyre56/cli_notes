# This file is used to set the database environment variables
# and the database url
# This file will be automatically executed by alembic when
# alembic migration commands are run

import os

from sqlalchemy import engine_from_config, pool
from alembic import context

from cli_notes.models import Base

# Alembic config object for accessing values in alembic.ini
alembic_config = context.config

# This is the data detailing the DB schema
target_metadata = Base.metadata

MYSQL_USER = os.getenv('MYSQL_USER')
sql_url = f"mysql+pymysql://{MYSQL_USER}@localhost/notesdb"
alembic_config.set_main_option("sqlalchemy.url", sql_url)


def run_migrations_offline() -> None:
    """
    Run migrations offline, meaning we
    do not need a valid DB connection and SQL
    commands can be executed once a connection
    is established.
    """
    url = alembic_config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named",
        },
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations online, meaning we do
    require a DB connection right now.
    """
    # Use a NullPool as we do not require persistent connections
    # so it's ok to open and close the DB connection each time
    connector = engine_from_config(
        alembic_config.get_section(alembic_config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connector.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
