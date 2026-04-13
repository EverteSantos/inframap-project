from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    role: str
    email: str
    login: str
    senha_hash: str
    status: str
    
class UsuarioCreate(UsuarioBase):
    senha_hash: str 

class UsuarioResponse(UsuarioBase):
    id: int
    
    class Config:
        from_attributes = True