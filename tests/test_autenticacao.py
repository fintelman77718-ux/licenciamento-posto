import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_registrar_usuario(cliente_teste: AsyncClient):
    """Testa registro de novo usuário."""
    response = await cliente_teste.post(
        "/auth/registrar",
        json={
            "email": "teste@exemplo.com",
            "nome_completo": "Teste User",
            "senha": "senha123",
        },
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "teste@exemplo.com"
    assert data["nome_completo"] == "Teste User"
    assert "id" in data


@pytest.mark.asyncio
async def test_registrar_email_duplicado(cliente_teste: AsyncClient):
    """Testa registro com email duplicado."""
    # Primeiro registro
    await cliente_teste.post(
        "/auth/registrar",
        json={
            "email": "teste@exemplo.com",
            "nome_completo": "Teste User",
            "senha": "senha123",
        },
    )
    
    # Segundo registro com mesmo email
    response = await cliente_teste.post(
        "/auth/registrar",
        json={
            "email": "teste@exemplo.com",
            "nome_completo": "Outro User",
            "senha": "senha456",
        },
    )
    
    assert response.status_code == 400
    assert "Email já registrado" in response.json()["detail"]


@pytest.mark.asyncio
async def test_login_sucesso(cliente_teste: AsyncClient):
    """Testa login bem-sucedido."""
    # Registrar usuário
    await cliente_teste.post(
        "/auth/registrar",
        json={
            "email": "teste@exemplo.com",
            "nome_completo": "Teste User",
            "senha": "senha123",
        },
    )
    
    # Fazer login
    response = await cliente_teste.post(
        "/auth/login",
        json={
            "email": "teste@exemplo.com",
            "senha": "senha123",
        },
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_login_senha_incorreta(cliente_teste: AsyncClient):
    """Testa login com senha incorreta."""
    # Registrar usuário
    await cliente_teste.post(
        "/auth/registrar",
        json={
            "email": "teste@exemplo.com",
            "nome_completo": "Teste User",
            "senha": "senha123",
        },
    )
    
    # Tentar login com senha errada
    response = await cliente_teste.post(
        "/auth/login",
        json={
            "email": "teste@exemplo.com",
            "senha": "senhaerrada",
        },
    )
    
    assert response.status_code == 401
    assert "Email ou senha incorretos" in response.json()["detail"]


@pytest.mark.asyncio
async def test_login_usuario_inexistente(cliente_teste: AsyncClient):
    """Testa login com usuário inexistente."""
    response = await cliente_teste.post(
        "/auth/login",
        json={
            "email": "inexistente@exemplo.com",
            "senha": "senha123",
        },
    )
    
    assert response.status_code == 401
    assert "Email ou senha incorretos" in response.json()["detail"]