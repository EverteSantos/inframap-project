from sqlalchemy import Column, String, Integer
from app.database.base import Base
from sqlalchemy.orm import relationship

class TipoAtivo(Base):
    __tablename__ = "tipo_ativos"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), unique=True, nullable=False)
    
    ativo = relationship('Ativo', back_populates='tipo_ativo')
