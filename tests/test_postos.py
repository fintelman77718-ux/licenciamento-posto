import pytest
from httpx import AsyncClient
from uuid import uuid4


@pytest.mark.asyncio
async def test_criar_posto(cliente_teste: AsyncClient):
    """Testa criação de um novo posto."""
    # Primeiro, registrar e fazer login
    await cliente_teste.post(
        "/auth/registrar",
        json={
            "email": "admin@exemplo.com",
            "nome_completo": "Admin User",
            "senha": "senha123",
        },
    )
    
    login_response = await cliente_teste.post(
        "/auth/login",
        json={
            "email": "admin@exemplo.com",
            "senha": "senha123",
        },
    )
    
    token = login_response.json()["access_token"]
    
    # Criar posto
    response = await cliente_teste.post(
        "/postos/",
        json={
            "nome": "Posto Shell Centro",
            "cnpj": "12.345.678/0001-90",
            "endereco": "Rua Principal, 100",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "cep": "20000-000",
            "latitude": -22.9068,
            "longitude": -43.1729,
            "telefone": "(21) 3333-3333",
            "email": "contato@posto.com",
            "descricao": "Posto de abastecimento",
            "ativo": "S",
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Posto Shell Centro"
    assert data["cnpj"] == "12.345.678/0001-90"


@pytest.mark.asyncio
async def test_listar_postos(cliente_teste: AsyncClient):
    """Testa listagem de postos."""
    # Registrar e fazer login
    await cliente_teste.post(
        "/auth/registrar",
        json={
            "email": "admin@exemplo.com",
            "nome_completo": "Admin User",
            "senha": "senha123",
        },
    )
    
    login_response = await cliente_teste.post(
        "/auth/login",
        json={
            "email": "admin@exemplo.com",
            "senha": "senha123",
        },
    )
    
    token = login_response.json()["access_token"]
    
    # Listar postos
    response = await cliente_teste.get(
        "/postos/",
        headers={"Authorization": f"Bearer {token}"},
    )
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)


@pytest.mark.asyncio
async def test_acessar_sem_token(cliente_teste: AsyncClient):
    """Testa acesso a endpoint protegido sem token."""
    response = await cliente_teste.get("/postos/")
    
    assert response.status_code == 403