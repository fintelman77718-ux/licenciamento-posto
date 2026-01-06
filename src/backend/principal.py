from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.backend.nucleo.configuracao import obter_configuracoes
from src.backend.api.rotas.autenticacao import roteador_autenticacao
from src.backend.api.rotas.postos import roteador_postos
from src.backend.api.rotas.processos import roteador_processos
from src.backend.api.rotas.etapas import roteador_etapas

configuracoes = obter_configuracoes()

aplicacao = FastAPI(
    title="Licenciamento de Postos",
    description="Sistema de gestão de licenciamento ambiental para postos de abastecimento",
    version="0.1.0",
)

aplicacao.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir roteadores
aplicacao.include_router(roteador_autenticacao)
aplicacao.include_router(roteador_postos)
aplicacao.include_router(roteador_processos)
aplicacao.include_router(roteador_etapas)


@aplicacao.get("/")
async def raiz():
    """Verificação de saúde."""
    return {"mensagem": "API de Licenciamento de Postos", "status": "online"}


@aplicacao.get("/saude")
async def saude():
    """Verificação de saúde detalhada."""
    return {
        "status": "saudável",
        "ambiente": configuracoes.ambiente,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.backend.principal:aplicacao",
        host=configuracoes.host_api,
        port=configuracoes.porta_api,
        reload=configuracoes.recarregar_api,
    )