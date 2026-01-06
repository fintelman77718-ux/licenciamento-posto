import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.backend.principal import aplicacao
from src.backend.bd.base import Base
from src.backend.bd.conexao import obter_sessao_bd
from src.backend.nucleo.configuracao import obter_configuracoes

configuracoes = obter_configuracoes()

# URL de teste (banco em memória)
DATABASE_URL_TEST = "sqlite+aiosqlite:///:memory:"


@pytest.fixture
async def engine_teste():
    """Cria engine de teste."""
    engine = create_async_engine(
        DATABASE_URL_TEST,
        echo=False,
        future=True,
    )
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    yield engine
    
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    
    await engine.dispose()


@pytest.fixture
async def sessao_teste(engine_teste):
    """Cria sessão de teste."""
    async_session = sessionmaker(
        engine_teste,
        class_=AsyncSession,
        expire_on_commit=False,
    )
    
    async with async_session() as sessao:
        yield sessao


@pytest.fixture
async def cliente_teste(sessao_teste):
    """Cria cliente HTTP de teste."""
    async def override_obter_sessao_bd():
        yield sessao_teste
    
    aplicacao.dependency_overrides[obter_sessao_bd] = override_obter_sessao_bd
    
    async with AsyncClient(app=aplicacao, base_url="http://test") as cliente:
        yield cliente
    
    aplicacao.dependency_overrides.clear()