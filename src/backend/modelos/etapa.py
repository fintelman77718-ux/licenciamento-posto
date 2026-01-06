from sqlalchemy import Column, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from src.backend.bd.base import Base


class EtapaBD(Base):
    """Modelo de etapa do processo de licenciamento."""
    
    __tablename__ = "etapas"
    
    id = Column(String, primary_key=True, index=True)
    processo_id = Column(String, ForeignKey("processos.id"), nullable=False, index=True)
    numero_etapa = Column(String, nullable=False)
    nome = Column(String, nullable=False)
    descricao = Column(Text, nullable=True)
    status = Column(String, default="pendente", nullable=False)  # "pendente", "em_progresso", "concluida"
    obrigatoria = Column(Boolean, default=True, nullable=False)
    data_inicio = Column(DateTime, nullable=True)
    data_conclusao = Column(DateTime, nullable=True)
    observacoes = Column(Text, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relacionamentos
    processo = relationship("ProcessoBD", back_populates="etapas")