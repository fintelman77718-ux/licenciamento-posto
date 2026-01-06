from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from src.backend.nucleo.configuracao import obter_configuracoes

configuracoes = obter_configuracoes()

# Contexto de criptografia
contexto_criptografia = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Algoritmo JWT
ALGORITMO = "HS256"


def hash_senha(senha: str) -> str:
    """Gera hash da senha."""
    return contexto_criptografia.hash(senha)


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """Verifica se a senha corresponde ao hash."""
    return contexto_criptografia.verify(senha, hash_senha)


def criar_token_acesso(dados: dict, expira_em: Optional[timedelta] = None) -> str:
    """Cria um token JWT de acesso."""
    para_codificar = dados.copy()
    
    if expira_em:
        expiracao = datetime.now(timezone.utc) + expira_em
    else:
        expiracao = datetime.now(timezone.utc) + timedelta(hours=24)
    
    para_codificar.update({"exp": expiracao})
    
    token_codificado = jwt.encode(
        para_codificar,
        configuracoes.chave_secreta,
        algorithm=ALGORITMO
    )
    
    return token_codificado


def verificar_token(token: str) -> Optional[dict]:
    """Verifica e decodifica um token JWT."""
    try:
        payload = jwt.decode(
            token,
            configuracoes.chave_secreta,
            algorithms=[ALGORITMO]
        )
        return payload
    except JWTError:
        return None