from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conection import get_db
from app.schemas.localizacao_schema import LocalizacaoCreate, LocalizacaoResponse
from app.models.localizacao import Localizacao

router = APIRouter(prefix='/localizacao', tags=['localizacoes'])

@router.post('/', response_model=LocalizacaoResponse, status_code=201)
def criar_localizacao(localizacao: LocalizacaoCreate, db: Session = Depends(get_db)):
    
    localizacao_db = db.query(Localizacao).filter(Localizacao.pop == localizacao.pop).first()
    
    if localizacao_db:
        raise HTTPException(status_code=400, detail='Localização já cadastrada.')
    
    nova_localizacao = Localizacao(
        pop = localizacao.pop,
        datacenter = localizacao.datacenter,
        rack = localizacao.rack,
        sala = localizacao.sala,
        cliente = localizacao.cliente        
    )
    
    db.add(nova_localizacao)
    db.commit()
    db.refresh(nova_localizacao)
    
    return nova_localizacao

@router.get('/', response_model=list[LocalizacaoResponse])
def listar_localizacoes(db: Session = Depends(get_db), limit: int = 10, offset: int = 0):
    
    localizacao_db = db.query(Localizacao).limit(limit).offset(offset).all()
    
    return localizacao_db

@router.get('/{localizacao_id}', response_model=LocalizacaoResponse)
def localizacao_por_id(localizacao_id: int, db: Session = Depends(get_db)):
    
    localizacao_db = db.query(Localizacao).filter(Localizacao.id == localizacao_id).first()
    
    if not localizacao_db:
        raise HTTPException(status_code=404, detail='Localização não existe.')
    
    return localizacao_db

@router.put('/{localizacao_id}', response_model=LocalizacaoResponse)
def atualizar_localizacao(localizacao_id: int, localizacao: LocalizacaoCreate, db: Session = Depends(get_db)):
    
    
    localizacao_db = db.query(Localizacao).filter(Localizacao.id == localizacao_id).first()
    
    if not localizacao_db:
        raise HTTPException(status_code=404, detail='Localização não existe.')
    
    localizacao_db.pop = localizacao.pop
    localizacao_db.rack = localizacao.rack
    localizacao_db.datacenter = localizacao.datacenter
    localizacao_db.sala = localizacao.sala
    localizacao_db.cliente = localizacao.cliente
    
    db.commit()
    db.refresh(localizacao_db)
    
    return localizacao_db

@router.delete('/{localizacao_id}', response_model=LocalizacaoResponse, status_code=204)
def deletar_localizacao(localizacao_id: int, db: Session = Depends(get_db)):
    
    localizacao_db = db.query(Localizacao).filter(Localizacao.id == localizacao_id).first()
    
    if not localizacao_db:
        raise HTTPException(status_code=404, detail='Localização não existe.')   
    
    db.delete(localizacao_db)
    db.commit()
    
    return None