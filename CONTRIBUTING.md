# 🤝 Contribuindo

Obrigado por querer contribuir! Siga os passos abaixo.

## 📋 Fluxo de trabalho

1. **Criar feature branch**
   \\\ash
   git checkout -b feature/nome-da-funcionalidade
   \\\

2. **Fazer alterações**
   - Edite os arquivos necessários
   - Mantenha o código limpo e bem documentado

3. **Fazer commit**
   \\\ash
   git add .
   git commit -m "tipo: descrição"
   \\\

4. **Fazer push**
   \\\ash
   git push -u origin feature/nome-da-funcionalidade
   \\\

5. **Criar Pull Request**
   - Vá para GitHub
   - Clique em "New pull request"
   - Descreva as mudanças

6. **Aguardar aprovação**
   - Os testes devem passar
   - Aguarde revisão

7. **Fazer merge**
   - Clique em "Merge pull request"
   - Selecione "Squash and merge"

## 📝 Padrões de commit

Use os seguintes prefixos:

- **feat:** Nova funcionalidade
  \\\
  feat: adicionar autenticação de usuários
  \\\

- **fix:** Correção de bug
  \\\
  fix: corrigir erro de validação
  \\\

- **docs:** Documentação
  \\\
  docs: atualizar README
  \\\

- **chore:** Tarefas de manutenção
  \\\
  chore: atualizar dependências
  \\\

## ✅ Checklist antes de fazer commit

- [ ] Código segue PEP 8
- [ ] Testes passam localmente
- [ ] Documentação atualizada
- [ ] Sem erros de linter (Ruff)
- [ ] Sem erros de type checking (Mypy)

## 🧪 Executar testes localmente

\\\ash
# Instalar dependências
pip install -r requirements.txt

# Executar linter
ruff check src/ tests/

# Executar type checker
mypy src/ --ignore-missing-imports

# Executar testes
pytest tests/ -v --cov=src
\\\

## 📞 Dúvidas?

Abra uma issue ou entre em contato com o desenvolvedor.
