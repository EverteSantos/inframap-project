from sqlalchemy import Column, String, Integer
from app.database.base import Base
from sqlalchemy.orm import relationship

class Fabricante(Base):
    __tablename__ = "fabricantes"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(80), unique=True, nullable=False)
    
    modelos = relationship('Modelo', back_populates='fabricante')
    