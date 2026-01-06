import asyncio
from src.backend.bd.conexao import engine
from src.backend.bd.base import Base
from src.backend.modelos import UsuarioBD, PostoBD, ProcessoBD, EtapaBD


async def criar_tabelas():
    """Cria todas as tabelas no banco de dados."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("✅ Tabelas criadas com sucesso!")


if __name__ == "__main__":
    asyncio.run(criar_tabelas())