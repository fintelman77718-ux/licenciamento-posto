# 📋 Configuração Atual do Repositório

**Data**: 6 de janeiro de 2026
**Versão**: 1.0
**Status**: Estável

---

## 🏗️ ESTRUTURA DO PROJETO

### Diretórios principais:
- **src/** - Código-fonte da aplicação
  - **backend/** - API FastAPI
  - **models/** - Modelos de dados (SQLAlchemy)
  - **schemas/** - Schemas Pydantic
  - **services/** - Lógica de negócio
  - **utils/** - Utilitários
  
- **tests/** - Testes automatizados
  - **unit/** - Testes unitários
  - **integration/** - Testes de integração
  
- **.github/workflows/** - Workflows do GitHub Actions
  - **tests.yml** - Pipeline de testes (Ruff, Mypy, Pytest)
  
- **docs/** - Documentação
  - **API.md** - Documentação da API

---

## 🔧 CONFIGURAÇÕES ATIVAS

### GitHub Rulesets
- **Nome**: Protect main branch
- **Status**: Active
- **Target**: main (default branch)
- **Regras**:
  - ✅ Require a pull request before merging
  - ✅ Block force pushes
  - ✅ Restrict deletions

### GitHub Actions
- **Workflow**: Tests
- **Trigger**: Push e Pull Request (todas as branches)
- **Passos**:
  1. Checkout code
  2. Setup Python 3.12
  3. Cache pip packages
  4. Install dependencies
  5. Run Ruff (linter)
  6. Run Mypy (type checker)
  7. Run Pytest (testes)
  8. Upload coverage to Codecov

### Dependências principais
- **FastAPI** 0.104+
- **SQLAlchemy** 2.0+
- **Pydantic** 2.0+
- **PostgreSQL** 15
- **Pytest** (testes)
- **Ruff** (linter)
- **Mypy** (type checker)

---

## 📊 STATUS DOS TESTES

- ✅ Ruff: Passando
- ✅ Mypy: Passando
- ✅ Pytest: Passando
- ✅ Coverage: Ativo

---

## 🔐 PROTEÇÕES ATIVAS

- ✅ Branch protection (main)
- ✅ Status checks obrigatórios
- ✅ Pull Request obrigatório
- ✅ Force push bloqueado
- ✅ Deleção de branch bloqueada

---

## 📝 FLUXO DE TRABALHO

1. Criar feature branch: `git checkout -b feature/nome`
2. Fazer alterações
3. Fazer commit: `git commit -m "tipo: descrição"`
4. Fazer push: `git push -u origin feature/nome`
5. Criar PR no GitHub
6. Aguardar testes passarem
7. Fazer merge (Squash and merge)
8. Deletar branch feature

---

## 🚨 PONTOS DE ATENÇÃO

- Nenhum push direto para main (bloqueado)
- Todos os PRs devem passar nos testes
- Documentação deve ser atualizada junto com código
- Cobertura de testes deve ser mantida

---

## 📞 CONTATO

Desenvolvedor: Luiz Fintelman
Especialidade: Engenharia Ambiental e Geotécnica