from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HistoricoAtivoBase(BaseModel):
    ativo_id: int
    usuario_id: int
    campo_alterado: str
    valor_antigo: Optional[str] = None
    valor_novo: Optional[str] = None
    tipo_acao: str
    observacao: Optional[str] = None
    
class HistoricoAtivoCreate(HistoricoAtivoBase):
    pass 

class HistoricoAtivoResponse(HistoricoAtivoBase):
    id: int
    data_alteracao: datetime
    
    class Config:
        from_attributes = True