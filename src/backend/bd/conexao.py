from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.backend.nucleo.configuracao import obter_configuracoes

configuracoes = obter_configuracoes()

# Converter URL PostgreSQL para async
url_bd_async = configuracoes.url_bd.replace(
    "postgresql://",
    "postgresql+asyncpg://"
)

# Criar engine assíncrono
engine = create_async_engine(
    url_bd_async,
    echo=configuracoes.ambiente == "desenvolvimento",
    future=True,
)

# Criar session factory
SessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def obter_sessao_bd():
    """Dependency para obter sessão do banco de dados."""
    async with SessionLocal() as sessao:
        try:
            yield sessao
        finally:
            await sessao.close()