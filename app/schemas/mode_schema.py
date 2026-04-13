from pydantic import BaseModel

class ModeloBase(BaseModel):
    nome: str
    fabricante_id: int
    
class ModeloCreate(ModeloBase):
    pass 

class ModeloResponse(ModeloBase):
    id: int
    
    class Config:
        from_attributes = True