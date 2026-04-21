from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.conection import get_db
from app.schemas.ativo_schema import AtivoCreate, AtivoResponse
from app.models.ativo import Ativo

router = APIRouter(prefix="/ativo", tags=['ativos'])

@router.post('/', response_model=AtivoResponse, status_code=201)
def criar_ativo(ativo: AtivoCreate, db: Session = Depends(get_db)):

    ativo_db = db.query(Ativo).filter(
        (Ativo.hostname == ativo.hostname) |
        (Ativo.numero_serie == ativo.numero_serie) |
        (Ativo.patrimonio == ativo.patrimonio) |
        (Ativo.ip_gerencia == ativo.ip_gerencia) |
        (Ativo.mac_add == ativo.mac_add)
    ).first()

    if ativo_db:
        raise HTTPException(status_code=400, detail='Já existe um ativo com dados únicos já cadastrados.')

    novo_ativo = Ativo(
        tipo_ativo_id=ativo.tipo_ativo_id,
        nome=ativo.nome,
        localizacao_id=ativo.localizacao_id,
        hostname=ativo.hostname.strip().upper(),
        descricao=ativo.descricao,
        modelo_id=ativo.modelo_id,
        numero_serie=ativo.numero_serie.strip(),
        patrimonio=ativo.patrimonio.strip(),
        ip_gerencia=ativo.ip_gerencia,
        vlan_gerencia=ativo.vlan_gerencia,
        mac_add=ativo.mac_add.strip().upper(),
        status=ativo.status.strip().lower(),
        data_aquisicao=ativo.data_aquisicao,
        data_implantacao=ativo.data_implantacao,
        observacao=ativo.observacao,
    )

    db.add(novo_ativo)
    db.commit()
    db.refresh(novo_ativo)

    return novo_ativo