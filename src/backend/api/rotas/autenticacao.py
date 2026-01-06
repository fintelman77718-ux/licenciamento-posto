from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from uuid import uuid4

from src.backend.bd.conexao import obter_sessao_bd
from src.backend.modelos.usuario import UsuarioBD
from src.backend.esquemas.usuario import UsuarioCriar, UsuarioResposta
from src.backend.esquemas.autenticacao import CredenciaisLogin, TokenResposta
from src.backend.nucleo.seguranca import (
    hash_senha,
    verificar_senha,
    criar_token_acesso,
)

roteador_autenticacao = APIRouter(prefix="/auth", tags=["autenticacao"])


@roteador_autenticacao.post(
    "/registrar",
    response_model=UsuarioResposta,
    status_code=status.HTTP_201_CREATED
)
async def registrar(
    dados: UsuarioCriar,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Registra um novo usuário."""
    # Verificar se email já existe
    resultado = await sessao.execute(
        select(UsuarioBD).where(UsuarioBD.email == dados.email)
    )
    usuario_existente = resultado.scalar_one_or_none()
    
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email já registrado"
        )
    
    novo_usuario = UsuarioBD(
        id=str(uuid4()),
        email=dados.email,
        nome_completo=dados.nome_completo,
        senha_hash=hash_senha(dados.senha),
        ativo=True,
    )
    
    sessao.add(novo_usuario)
    await sessao.commit()
    await sessao.refresh(novo_usuario)
    
    return novo_usuario


@roteador_autenticacao.post("/login", response_model=TokenResposta)
async def login(
    credenciais: CredenciaisLogin,
    sessao: AsyncSession = Depends(obter_sessao_bd)
):
    """Realiza login e retorna token JWT."""
    resultado = await sessao.execute(
        select(UsuarioBD).where(UsuarioBD.email == credenciais.email)
    )
    usuario = resultado.scalar_one_or_none()
    
    if not usuario or not verificar_senha(credenciais.senha, usuario.senha_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos"
        )
    
    if not usuario.ativo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário inativo"
        )
    
    token = criar_token_acesso(dados={"sub": usuario.id})
    
    return {"access_token": token, "token_type": "bearer"}