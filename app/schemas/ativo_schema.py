from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AtivoBase(BaseModel):
    tipo_ativo_id: int
    nome: str
    localizacao_id: int
    hostname: str
    descricao: Optional[str]
    modelo_id: int
    numero_serie: str
    patrimonio: str
    ip_gerencia: str
    vlan_gerencia: Optional[int] = None
    mac_add: str
    status: str
    observacao: Optional[str]
    data_criacao: datetime
    data_atualizacao: datetime
    
class AtivoCreate(AtivoBase):
    pass
    
class AtivoResponse(AtivoBase):
    id: int
    data_aquisicao: datetime
    data_implantacao: datetime
  
    class Config:
        from_attributes = True

    