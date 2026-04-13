from sqlalchemy import Column, String, Integer, ForeignKey
from app.database.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Date, DateTime
from datetime import datetime

class Ativo(Base):
    __tablename__ = 'ativos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_ativo_id = Column(Integer, ForeignKey('tipo_ativos.id'), nullable=False)
    nome = Column(String(150), nullable=False)
    localizacao_id = Column(Integer, ForeignKey('localizacoes.id'), nullable=False)
    hostname = Column(String(150), nullable=False, unique=True)
    descricao = Column(String(255), nullable=True)
    modelo_id = Column(Integer, ForeignKey('modelos.id'), nullable=False)
    numero_serie = Column(String(100), unique=True, nullable=False)
    patrimonio = Column(String(100), nullable=False, unique=True)
    ip_gerencia = Column(String(45), unique=True, nullable=False)
    vlan_gerencia = Column(Integer, nullable=True)
    mac_add = Column(String(17), unique=True, nullable=False)
    status = Column(String(50), nullable=False)
    data_aquisicao = Column(DateTime, nullable=False)
    data_implantacao = Column(DateTime, nullable=False)
    observacao = Column(String(500), nullable=True)
    data_criacao = Column(DateTime, default=datetime.utcnow, nullable=False)
    data_atualizacao = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    
    tipo_ativo = relationship("TipoAtivo", back_populates='ativos')
    modelo = relationship('Modelo', back_populates='ativos')
    localizacao = relationship('Localizacao', back_populates='ativos')
    historicos = relationship('HistoricoAtivo', back_populates='ativo')
    

           
    