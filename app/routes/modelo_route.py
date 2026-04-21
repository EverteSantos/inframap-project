from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conection import get_db
from app.schemas.modelo_schema import ModeloCreate, ModeloResponse
from app.models.modelo import Modelo 
from app.models.fabricante import Fabricante

router = APIRouter(prefix='/modelo', tags=['modelos'])

@router.post('/', response_model=ModeloResponse, status_code=201)
def criar_modelo(modelo: ModeloCreate, db: Session = Depends(get_db)):
    
    modelo_db = db.query(Modelo).filter(Modelo.nome == modelo.nome).first()
    
    if modelo_db:
        raise HTTPException(status_code=400, detail='Modelo já existe.')
    
    fabricante_db = db.query(Fabricante).filter(Fabricante.id == modelo.fabricante_id).first()
    
    if not fabricante_db:
        raise HTTPException(status_code=404, detail="Fabricante não encontrado.")
    
    novo_modelo = Modelo(
        nome = modelo.nome,
        fabricante = fabricante_db
    )
    
    db.add(novo_modelo)
    db.commit()
    db.refresh(novo_modelo)
    
    return novo_modelo

@router.get('/', response_model=list[ModeloResponse])
def listar_modelos(db: Session = Depends(get_db), limit: int = 10, offset: int = 0):
    modelos_db = db.query(Modelo).limit(limit).offset(offset).all()
    
    return modelos_db

@router.get('/{modelo_id}', response_model=ModeloResponse)
def modelo_por_id(modelo_id: int, db: Session = Depends(get_db)):
    
    modelo_db = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    
    if not modelo_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado.")
    
    return modelo_db

@router.put('/{modelo_id}', response_model=ModeloResponse)
def atualizar_modelo(modelo_id: int, modelo: ModeloCreate, db: Session = Depends(get_db)):
    
    modelo_db = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    
    if not modelo_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado.")
    
    modelo_db.nome = modelo.nome.strip().title()
    
    db.commit()
    db.refresh(modelo_db)
    
    return modelo_db

@router.delete('/{modelo_id}', status_code=204)
def deletar_modelo(modelo_id: int, db: Session = Depends(get_db)):
    
    modelo_db = db.query(Modelo).filter(Modelo.id == modelo_id).first()
    if not modelo_db:
        raise HTTPException(status_code=404, detail="Modelo não encontrado.")
    
    db.delete(modelo_db)
    db.commit()
    
    return None
    