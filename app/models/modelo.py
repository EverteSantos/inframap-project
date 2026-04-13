from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Modelo(Base):
    __tablename__ = "modelos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, unique=True, nullable=False)
    fabricante_id = Column(Integer, ForeignKey('fabricantes.id'), nullable=False)
    
    fabricante = relationship("Fabricante", back_populates='modelos')
    ativos = relationship('Ativo', back_populates='modelo')