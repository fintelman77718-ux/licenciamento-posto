from sqlalchemy import Column, String, Float, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from src.backend.bd.base import Base


class PostoBD(Base):
    """Modelo de posto de abastecimento."""
    
    __tablename__ = "postos"
    
    id = Column(String, primary_key=True, index=True)
    nome = Column(String, nullable=False, index=True)
    cnpj = Column(String, unique=True, nullable=False, index=True)
    endereco = Column(String, nullable=False)
    cidade = Column(String, nullable=False, index=True)
    estado = Column(String, nullable=False)
    cep = Column(String, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    telefone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    descricao = Column(Text, nullable=True)
    ativo = Column(String, default="ativo", nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow, nullable=False)
    atualizado_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    # Relacionamentos
    processos = relationship("ProcessoBD", back_populates="posto")