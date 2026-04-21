from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conection import get_db
from app.schemas.tipo_ativo_schema import TipoAtivoCreate, TipoAtivoResponse
from app.models.tipo_ativo import TipoAtivo

router = APIRouter(prefix='/tipo_ativo', tags = ['tipo_ativos'])

@router.post('/', response_model = TipoAtivoResponse, status_code=201)
def definir_tipo_ativo(tipo_ativo: TipoAtivoCreate, db: Session = Depends(get_db)):
    
    tipo_ativo_db = db.query(TipoAtivo).filter(TipoAtivo.nome == tipo_ativo.nome).first()

    if tipo_ativo_db:
        raise HTTPException(status_code=400, detail="Tipo de ativo já cadastrado.")

    novo_tipo_ativo = TipoAtivo(
        nome = tipo_ativo.nome.strip().title()
    )

    db.add(novo_tipo_ativo)
    db.commit()
    db.refresh(novo_tipo_ativo)

    return novo_tipo_ativo

@router.get('/', response_model = list[TipoAtivoResponse])
def listar_tipo_ativos(db: Session = Depends(get_db), limit: int = 10, offset: int = 0):

    lista_tipo_ativos = db.query(TipoAtivo).limit(limit).offset(offset).all()


    return lista_tipo_ativos

@router.get('/{tipo_ativo_id}', response_model=TipoAtivoResponse)
def busca_por_id(tipo_ativo_id: int, db: Session = Depends(get_db)):

    busca_ativo_id = db.query(TipoAtivo).filter(TipoAtivo.id == tipo_ativo_id).first()

    if not busca_ativo_id:
        raise HTTPException(status_code=404, detail='ID não existe.')

    return busca_ativo_id

@router.put('/{tipo_ativo_id}', response_model=TipoAtivoResponse)
def atualizar_tipo_ativo(tipo_ativo_id: int, tipo_ativo: TipoAtivoCreate, db: Session = Depends(get_db)):
    
    tipo_ativo_db = db.query(TipoAtivo).filter(TipoAtivo.id == tipo_ativo_id).first()

                                                  
    if not tipo_ativo_db:
        raise HTTPException(status_code = 404, detail='Tipo de ativo não encontrado.')
    
    tipo_ativo_db.nome = tipo_ativo.nome.strip().title()
    
    db.commit()
    db.refresh(tipo_ativo_db)
    
    return tipo_ativo_db

@router.delete('/{tipo_ativo_id}', response_model=TipoAtivoResponse, status_code=204)
def deletar_tipo_ativo(tipo_ativo_id: int, db: Session = Depends(get_db)):
    
    tipo_ativo_db = db.query(TipoAtivo).filter(TipoAtivo.id == tipo_ativo_id).first()
                                                 
    if not tipo_ativo_db:
        raise HTTPException(status_code = 404, detail='Tipo de ativo não encontrado.')
    
    db.delete(tipo_ativo_db)
    db.commit()
    
    return None
    
    