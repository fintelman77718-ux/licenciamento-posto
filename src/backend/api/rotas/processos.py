from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import uuid4
from src.backend.bd.conexao import obter_sessao_bd
from src.backend.modelos.processo import ProcessoBD
from src.backend.esquemas.processo import ProcessoCriar, ProcessoAtualizar, ProcessoResposta

roteador_processos = APIRouter(prefix="/processos", tags=["processos"])


@roteador_processos.get("/", response_model=list[ProcessoResposta])
async def listar_processos(sessao: AsyncSession = Depends(obter_sessao_bd)):
    """Lista todos os processos."""
    resultado = await sessao.execute(select(ProcessoBD))
    processos = resultado.scalars().all()
    return processos


@roteador_processos.get("/{processo_id}", response_model=ProcessoResposta)
async def obter_processo(
    processo_id: str,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Obtém um processo específico."""
    resultado = await sessao.execute(
        select(ProcessoBD).where(ProcessoBD.id == processo_id)
    )
    processo = resultado.scalar_one_or_none()
    
    if not processo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processo não encontrado"
        )
    
    return processo


@roteador_processos.post("/", response_model=ProcessoResposta, status_code=status.HTTP_201_CREATED)
async def criar_processo(
    dados: ProcessoCriar,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Cria um novo processo."""
    novo_processo = ProcessoBD(
        id=str(uuid4()),
        **dados.dict()
    )
    sessao.add(novo_processo)
    await sessao.commit()
    await sessao.refresh(novo_processo)
    return novo_processo


@roteador_processos.put("/{processo_id}", response_model=ProcessoResposta)
async def atualizar_processo(
    processo_id: str,
    dados: ProcessoAtualizar,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Atualiza um processo existente."""
    resultado = await sessao.execute(
        select(ProcessoBD).where(ProcessoBD.id == processo_id)
    )
    processo = resultado.scalar_one_or_none()
    
    if not processo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processo não encontrado"
        )
    
    dados_atualizacao = dados.dict(exclude_unset=True)
    for campo, valor in dados_atualizacao.items():
        setattr(processo, campo, valor)
    
    await sessao.commit()
    await sessao.refresh(processo)
    return processo


@roteador_processos.delete("/{processo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_processo(
    processo_id: str,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Deleta um processo."""
    resultado = await sessao.execute(
        select(ProcessoBD).where(ProcessoBD.id == processo_id)
    )
    processo = resultado.scalar_one_or_none()
    
    if not processo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Processo não encontrado"
        )
    
    await sessao.delete(processo)
    await sessao.commit()