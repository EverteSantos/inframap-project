from pydantic import BaseModel

class TipoAtivoBase(BaseModel):
    nome: str
    
class TipoAtivoCreate(TipoAtivoBase):
    pass 

class TipoAtivoResponse(TipoAtivoBase):
    id: int
    
    class Config:
        from_attributes = True

