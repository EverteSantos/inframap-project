from sqlalchemy import Column, String, Integer
from app.database.base import Base
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150), nullable=False)
    role = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False)
    login = Column(String(100), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    status = Column(String(20), nullable=False)
    
    historicos = relationship('HistoricoAtivo', back_populates='usuarios')
    
    