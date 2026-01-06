from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class EtapaBase(BaseModel):
    """Schema base de etapa."""
    processo_id: str
    numero_etapa: str
    nome: str
    descricao: Optional[str] = None
    obrigatoria: bool = True


class EtapaCriar(EtapaBase):
    """Schema para criar etapa."""
    pass


class EtapaAtualizar(BaseModel):
    """Schema para atualizar etapa."""
    status: Optional[str] = None
    data_inicio: Optional[datetime] = None
    data_conclusao: Optional[datetime] = None
    observacoes: Optional[str] = None


class EtapaResposta(EtapaBase):
    """Schema de resposta de etapa."""
    id: str
    status: str
    data_inicio: Optional[datetime]
    data_conclusao: Optional[datetime]
    observacoes: Optional[str]
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True