from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ProcessoBase(BaseModel):
    """Schema base de processo."""
    numero_processo: str
    posto_id: str
    usuario_id: str
    tipo_processo: str
    status: str = "em_analise"
    descricao: Optional[str] = None


class ProcessoCriar(ProcessoBase):
    """Schema para criar processo."""
    pass


class ProcessoAtualizar(BaseModel):
    """Schema para atualizar processo."""
    status: Optional[str] = None
    descricao: Optional[str] = None
    data_conclusao: Optional[datetime] = None


class ProcessoResposta(ProcessoBase):
    """Schema de resposta de processo."""
    id: str
    data_inicio: datetime
    data_conclusao: Optional[datetime]
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True