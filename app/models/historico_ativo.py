from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from app.database.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime

class HistoricoAtivo(Base):
    __tablename__ = 'historico_ativos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    ativo_id = Column(Integer, ForeignKey('ativos.id'), nullable=False)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    campo_alterado = Column(String(100), nullable=False)
    valor_antigo = Column(String(255), nullable=True)
    valor_novo = Column(String(255), nullable=True)
    tipo_acao = Column(String(50), nullable=False)
    observacao = Column(String(500), nullable=True)
    data_alteracao = Column(DateTime, default=datetime.utcnow,nullable=False)
    
    ativo = relationship('Ativo', back_populates='historico_ativos')
    usuario = relationship('Usuario', back_populates='historico_ativos')
    