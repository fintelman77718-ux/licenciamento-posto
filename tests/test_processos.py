import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_criar_processo(cliente_teste: AsyncClient):
    """Testa criação de um novo processo."""
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
    
    # Criar posto primeiro
    posto_response = await cliente_teste.post(
        "/postos/",
        json={
            "nome": "Posto Teste",
            "cnpj": "12.345.678/0001-90",
            "endereco": "Rua Teste, 100",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "cep": "20000-000",
            "ativo": "S",
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    
    posto_id = posto_response.json()["id"]
    
    # Criar processo
    response = await cliente_teste.post(
        "/processos/",
        json={
            "numero_processo": "2026/001",
            "posto_id": posto_id,
            "usuario_id": "user-id-aqui",
            "tipo_processo": "LICENCIAMENTO",
            "status": "EM_ANDAMENTO",
            "descricao": "Processo de licenciamento ambiental",
        },
        headers={"Authorization": f"Bearer {token}"},
    )
    
    assert response.status_code == 201
    data = response.json()
    assert data["numero_processo"] == "2026/001"