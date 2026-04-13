from sqlalchemy import Column, String, Integer
from app.database.base import Base
from sqlalchemy.orm import relationship

class Localizacao(Base):
    __tablename__ = 'localizacoes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    pop = Column(String(150), nullable=False)
    datacenter = Column(String(100), nullable=True)
    rack = Column(String(50), nullable=False)
    sala = Column(String(100), nullable=True)
    cliente = Column(String(150), nullable=True)
    
    ativos = relationship('Ativo', back_populates='localizacao')