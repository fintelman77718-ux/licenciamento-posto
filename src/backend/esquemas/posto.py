from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PostoBase(BaseModel):
    """Schema base de posto."""
    nome: str
    cnpj: str
    endereco: str
    cidade: str
    estado: str
    cep: str
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    descricao: Optional[str] = None


class PostoCriar(PostoBase):
    """Schema para criar posto."""
    pass


class PostoAtualizar(BaseModel):
    """Schema para atualizar posto."""
    nome: Optional[str] = None
    endereco: Optional[str] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    cep: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    descricao: Optional[str] = None
    ativo: Optional[str] = None


class PostoResposta(PostoBase):
    """Schema de resposta de posto."""
    id: str
    ativo: str
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True