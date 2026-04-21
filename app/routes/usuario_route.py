from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conection import get_db
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from app.models.usuario import Usuario


router = APIRouter(prefix='/usuario', tags=['usuarios'])



@router.post('/', response_model=UsuarioResponse, status_code=201)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    
    usuario_db = db.query(Usuario).filter(Usuario.nome == usuario.nome).first()
    
    if usuario_db:
        raise HTTPException(status_code=400, detail='Localização já cadastrada.')
    
    novo_usuario = Usuario(
        nome = usuario.nome,
        role = usuario.role,
        email = usuario.email,
        sala = usuario.login,
        senha_hash =  usuario.senha_hash,
        status = usuario.status       
    )
    
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    
    return novo_usuario

@router.get('/', response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db), limit: int = 10, offset: int = 0):
    
    usuario_db = db.query(Usuario).limit(limit).offset(offset).all()
    
    return usuario_db

@router.get('/{usuario_id}', response_model=UsuarioResponse)
def usuario_por_id(usuario_id: int, db: Session = Depends(get_db)):
    
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    if not usuario_db:
        raise HTTPException(status_code=404, detail='Localização não existe.')
    
    return  usuario_db

@router.put('/{usuario_id}', response_model=UsuarioResponse)
def atualizar_usuario(usuario_id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    
    
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    if not usuario_db:
        raise HTTPException(status_code=404, detail='Localização não existe.')
    
    usuario_db.nome = usuario.nome
    usuario_db.role = usuario.role
    usuario_db.email = usuario.email
    usuario_db.sala = usuario.login
    usuario_db.senha_hash =  usuario.senha_hash
    usuario_db.status = usuario.status
    
    db.commit()
    db.refresh(usuario_db)
    
    return usuario_db

@router.delete('/{usuario_id}', response_model=UsuarioResponse, status_code=204)
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    
    usuario_db = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    
    if not usuario_db:
        raise HTTPException(status_code=404, detail='Usuário não existe.')   
    
    db.delete(usuario_db)
    db.commit()
    
    return None