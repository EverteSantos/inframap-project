from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conection import get_db
from app.schemas.fabricante_schema import FabricanteCreate, FabricanteResponse
from app.models.fabricante import Fabricante

router = APIRouter(prefix='/fabricante', tags=['fabricantes'])

@router.post('/', response_model=Fabricante, status_code=201)
def criar_fabricante(fabricante: FabricanteCreate, db: Session = Depends(get_db)):
    
    fabricante_db = db.query(Fabricante).filter(Fabricante.nome == fabricante.nome.strip().title()).first()
    
    if fabricante_db:
        raise HTTPException(status_code=400, detail='Fabricante já existente.')
    
    novo_fabricante = Fabricante(
        nome = fabricante.nome.strip().title()
    )
    
    db.add(novo_fabricante)
    db.commit()
    db.refresh(novo_fabricante)
    
    return novo_fabricante

@router.get('/', response_model=list[FabricanteResponse])
def listar_fabricantes(db: Session = Depends(get_db), limit: int = 10, offset: int = 0):
    
    fabricante_db = db.query(Fabricante).limit(limit).offset(offset).all()
    
    return fabricante_db

@router.get('/{fabricante_id}', response_model=FabricanteResponse)
def fabricante_por_id(fabricante_id: int, db: Session = Depends(get_db)):
    
    fabricante_db = db.query(Fabricante).filter(Fabricante.id == fabricante_id).first()
    
    if not fabricante_db:
        raise HTTPException(status_code=404, detail=f"Fabricante com ID {fabricante_id} não encontrado")
    
    return fabricante_db

@router.put('/{fabricante_id}', response_model=FabricanteResponse)
def atualizar_fabricante(fabricante_id: int, fabricante: FabricanteCreate, db: Session = Depends(get_db)):
    
    fabricante_db = db.query(Fabricante).filter(Fabricante.id == fabricante_id).first()
    
    if not fabricante_db:
        raise HTTPException(status_code=404, detail="Fabricante não encontrado.")
    
    fabricante_db.nome = fabricante.nome.strip().title()
    
    db.commit()
    db.refresh(fabricante_db)
    
    return fabricante_db

@router.delete('/{fabricante_id}', response_model=FabricanteResponse, status_code=204)
def deletar_fabricante(fabricante_id: int, db: Session = Depends(get_db)):
    
    fabricante_db = db.query(Fabricante).filter(Fabricante.id == fabricante_id).first()
    
    if not fabricante_db:
        raise HTTPException(status_code=404, detail="Fabricante não existe.")
    
    db.delete(fabricante_db)
    db.commit()
    
    return None

    
    
    