from pydantic import BaseModel, EmailStr


class TokenResposta(BaseModel):
    """Schema de resposta de token."""
    access_token: str
    token_type: str = "bearer"


class CredenciaisLogin(BaseModel):
    """Schema de credenciais de login."""
    email: EmailStr
    senha: str


class UsuarioLogin(BaseModel):
    """Schema de usuário para login."""
    id: str
    email: str
    nome_completo: str