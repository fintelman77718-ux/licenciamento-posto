from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UsuarioBase(BaseModel):
    """Schema base de usuário."""
    email: EmailStr
    nome_completo: str


class UsuarioCriar(UsuarioBase):
    """Schema para criar usuário."""
    senha: str


class UsuarioAtualizar(BaseModel):
    """Schema para atualizar usuário."""
    nome_completo: Optional[str] = None
    email: Optional[EmailStr] = None
    ativo: Optional[bool] = None


class UsuarioResposta(UsuarioBase):
    """Schema de resposta de usuário."""
    id: str
    ativo: bool
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True