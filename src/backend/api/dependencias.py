from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.backend.bd.conexao import obter_sessao_bd
from src.backend.modelos.usuario import UsuarioBD
from src.backend.nucleo.seguranca import verificar_token

security = HTTPBearer()


async def obter_usuario_atual(
    credenciais: HTTPAuthorizationCredentials = Depends(security),
    sessao: AsyncSession = Depends(obter_sessao_bd)
) -> UsuarioBD:
    """Obtém o usuário atual a partir do token JWT."""
    token = credenciais.credentials
    
    payload = verificar_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    usuario_id: str = payload.get("sub")
    if not usuario_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    resultado = await sessao.execute(
        select(UsuarioBD).where(UsuarioBD.id == usuario_id)
    )
    usuario = resultado.scalar_one_or_none()
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return usuario