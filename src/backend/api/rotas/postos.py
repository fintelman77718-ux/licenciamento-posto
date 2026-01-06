from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import uuid4
from src.backend.bd.conexao import obter_sessao_bd
from src.backend.modelos.posto import PostoBD
from src.backend.modelos.usuario import UsuarioBD
from src.backend.esquemas.posto import PostoCriar, PostoAtualizar, PostoResposta
from src.backend.api.dependencias import obter_usuario_atual

roteador_postos = APIRouter(prefix="/postos", tags=["postos"])


@roteador_postos.get("/", response_model=list[PostoResposta])
async def listar_postos(
    usuario_atual: UsuarioBD = Depends(obter_usuario_atual),
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Lista todos os postos."""
    resultado = await sessao.execute(select(PostoBD))
    postos = resultado.scalars().all()
    return postos


@roteador_postos.get("/{posto_id}", response_model=PostoResposta)
async def obter_posto(
    posto_id: str,
    usuario_atual: UsuarioBD = Depends(obter_usuario_atual),
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Obtém um posto específico."""
    resultado = await sessao.execute(
        select(PostoBD).where(PostoBD.id == posto_id)
    )
    posto = resultado.scalar_one_or_none()
    
    if not posto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Posto não encontrado"
        )
    
    return posto


@roteador_postos.post("/", response_model=PostoResposta, status_code=status.HTTP_201_CREATED)
async def criar_posto(
    dados: PostoCriar,
    usuario_atual: UsuarioBD = Depends(obter_usuario_atual),
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Cria um novo posto."""
    novo_posto = PostoBD(
        id=str(uuid4()),
        **dados.model_dump()
    )
    sessao.add(novo_posto)
    await sessao.commit()
    await sessao.refresh(novo_posto)
    return novo_posto


@roteador_postos.put("/{posto_id}", response_model=PostoResposta)
async def atualizar_posto(
    posto_id: str,
    dados: PostoAtualizar,
    usuario_atual: UsuarioBD = Depends(obter_usuario_atual),
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Atualiza um posto existente."""
    resultado = await sessao.execute(
        select(PostoBD).where(PostoBD.id == posto_id)
    )
    posto = resultado.scalar_one_or_none()
    
    if not posto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Posto não encontrado"
        )
    
    dados_atualizacao = dados.model_dump(exclude_unset=True)
    for campo, valor in dados_atualizacao.items():
        setattr(posto, campo, valor)
    
    await sessao.commit()
    await sessao.refresh(posto)
    return posto


@roteador_postos.delete("/{posto_id}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar_posto(
    posto_id: str,
    usuario_atual: UsuarioBD = Depends(obter_usuario_atual),
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Deleta um posto."""
    resultado = await sessao.execute(
        select(PostoBD).where(PostoBD.id == posto_id)
    )
    posto = resultado.scalar_one_or_none()
    
    if not posto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Posto não encontrado"
        )
    
    await sessao.delete(posto)
    await sessao.commit()