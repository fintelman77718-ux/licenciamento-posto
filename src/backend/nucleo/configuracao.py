from pydantic_settings import BaseSettings
from typing import Literal


class Configuracoes(BaseSettings):
    """Configura��es da aplica��o."""

    # Ambiente
    ambiente: Literal["desenvolvimento", "producao"] = "desenvolvimento"

    # API
    host_api: str = "0.0.0.0"
    porta_api: int = 8000
    recarregar_api: bool = True

    # Banco de dados
    bd_usuario: str = "licenciamento"
    bd_senha: str = "senha_segura_123"
    bd_host: str = "localhost"
    bd_porta: int = 5432
    bd_nome: str = "licenciamento_db"
    url_bd: str = "postgresql://licenciamento:senha_segura_123@localhost:5432/licenciamento_db"

    # Redis
    redis_url: str = "redis://localhost:6379/0"

    # JWT
    chave_secreta: str = "sua-chave-secreta-super-segura-aqui-mude-em-producao"
    algoritmo_jwt: str = "HS256"
    tempo_expiracao_token: int = 24  # horas

    class Config:
        env_file = ".env"
        case_sensitive = False


def obter_configuracoes() -> Configuracoes:
    """Retorna as configura��es da aplica��o."""
    return Configuracoes()
