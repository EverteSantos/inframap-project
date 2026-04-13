from pydantic import BaseModel
from typing import Optional

class LocalizacaoBase(BaseModel):
    pop: str
    datacenter: Optional[str] = None
    rack: str
    sala: Optional[str] = None
    cliente: Optional[str] = None

class LocalizacaoCreate(LocalizacaoBase):
    pass

class LocalizacaoResponse(LocalizacaoBase):
    id: int
    
    class Config:
        from_attributes = True