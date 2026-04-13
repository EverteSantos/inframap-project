from pydantic import BaseModel

class FabricanteBase(BaseModel):
    nome: str
    
class FabricanteCreate(FabricanteBase):
    pass 

class FabricanteResponse(FabricanteBase):
    id: int
    
    class Config:
        from_attributes = True