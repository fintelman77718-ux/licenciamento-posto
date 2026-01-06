from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
from src.backend.bd.base import Base
from src.backend.nucleo.configuracao import obter_configuracoes

# Configurações
config = context.config
configuracoes = obter_configuracoes()

# Configurar logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Definir target_metadata
target_metadata = Base.metadata

# Configurar URL do banco
config.set_main_option("sqlalchemy.url", configuracoes.url_bd)


def run_migrations_offline() -> None:
    """Executar migrações em modo 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executar migrações em modo 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()