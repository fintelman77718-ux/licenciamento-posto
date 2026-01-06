# Criar pasta docs
New-Item -ItemType Directory -Path docs -Force

# Criar arquivo API.md
@"
# Documentação da API - Licenciamento Ambiental

## Autenticação

### Registrar novo usuário
\`\`\`bash
curl -X POST http://localhost:8000/auth/registrar \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@exemplo.com",
    "nome_completo": "João Silva",
    "senha": "senha123"
  }'
\`\`\`

### Fazer login
\`\`\`bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "usuario@exemplo.com",
    "senha": "senha123"
  }'
\`\`\`

**Resposta**:
\`\`\`json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
\`\`\`

## Postos de Combustível

### Criar novo posto
\`\`\`bash
curl -X POST http://localhost:8000/postos/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer {token}" \
  -d '{
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
    "ativo": "S"
  }'
\`\`\`

### Listar postos
\`\`\`bash
curl -X GET http://localhost:8000/postos/ \
  -H "Authorization: Bearer {token}"
\`\`\`

## Swagger UI

Acesse a documentação interativa em:
\`http://localhost:8000/docs\`
"@ | Set-Content docs/API.md