from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from src.backend.bd.base import Base


class ProcessoBD(Base):
    """Modelo de processo de licenciamento."""
    
    __tablename__ = "processos"
    
    id = Column(String, primary_key=True, index=True)
    numero_processo = Column(String, unique=True, nullable=False, index=True)
    posto_id = Column(String, ForeignKey("postos.id"), nullable=False, index=True)
    usuario_id = Column(String, ForeignKey("usuarios.id"), nullable=False, index=True)
    tipo_processo = Column(String, nullable=False)  # "licenciamento", "renovacao", "encerramento"
    status = Column(String, default="em_analise", nullable=False, index=True)  # "em_analise", "aprovado", "rejeitado"
    descricao = Column(Text, nullable=True)
    data_inicio = Column(DateTime, default=datetime.utcnow, nullable=False)
    data_conclusao = Column(DateTime, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relacionamentos
    posto = relationship("PostoBD", back_populates="processos")
    usuario = relationship("UsuarioBD", back_populates="processos")
    etapas = relationship("EtapaBD", back_populates="processo")