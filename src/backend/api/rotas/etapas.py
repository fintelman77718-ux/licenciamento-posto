from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import uuid4
from src.backend.bd.conexao import obter_sessao_bd
from src.backend.modelos.etapa import EtapaBD
from src.backend.esquemas.etapa import EtapaCriar, EtapaAtualizar, EtapaResposta

roteador_etapas = APIRouter(prefix="/etapas", tags=["etapas"])


@roteador_etapas.get("/", response_model=list[EtapaResposta])
async def listar_etapas(sessao: AsyncSession = Depends(obter_sessao_bd)):
    """Lista todas as etapas."""
    resultado = await sessao.execute(select(EtapaBD))
    etapas = resultado.scalars().all()
    return etapas


@roteador_etapas.get("/{etapa_id}", response_model=EtapaResposta)
async def obter_etapa(
    etapa_id: str,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Obtém uma etapa específica."""
    resultado = await sessao.execute(
        select(EtapaBD).where(EtapaBD.id == etapa_id)
    )
    etapa = resultado.scalar_one_or_none()
    
    if not etapa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Etapa não encontrada"
        )
    
    return etapa


@roteador_etapas.post("/", response_model=EtapaResposta, status_code=status.HTTP_201_CREATED)
async def criar_etapa(
    dados: EtapaCriar,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Cria uma nova etapa."""
    nova_etapa = EtapaBD(
        id=str(uuid4()),
        **dados.dict()
    )
    sessao.add(nova_etapa)
    await sessao.commit()
    await sessao.refresh(nova_etapa)
    return nova_etapa


@roteador_etapas.put("/{etapa_id}", response_model=EtapaResposta)
async def atualizar_etapa(
    etapa_id: str,
    dados: EtapaAtualizar,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Atualiza uma etapa existente."""
    resultado = await sessao.execute(
        select(EtapaBD).where(EtapaBD.id == etapa_id)
    )
    etapa = resultado.scalar_one_or_none()
    
    if not etapa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Etapa não encontrada"
        )
    
    dados_atualizacao = dados.dict(exclude_unset=True)
    for campo, valor in dados_atualizacao.items():
        setattr(etapa, campo, valor)
    
    await sessao.commit()
    await sessao.refresh(etapa)
    return etapa


@roteador_etapas.delete("/{etapa_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_etapa(
    etapa_id: str,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Deleta uma etapa."""
    resultado = await sessao.execute(
        select(EtapaBD).where(EtapaBD.id == etapa_id)
    )
    etapa = resultado.scalar_one_or_none()
    
    if not etapa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Etapa não encontrada"
        )
    
    await sessao.delete(etapa)
    await sessao.commit()