# Código da Aplicação

Esta pasta contém o código do seu agente financeiro.

## Estrutura Sugerida

```
bash
- #1. Instalar Ollama (ollama.com)
- #2. Baixar un modelo leve
- ollama pull gpt-oss
- #3. Testar se funciona
ollana run gpt-oss "Olá!"
```

## Código Completo

```
Todo o código-fonte está no arquivo 'app.py'
```

## Como Rodar

```bash
bash
# 1. Instalar dependências
pip install streamlit pandas requests
# 2. Garantir que Ollama esté rodando
ollana serve
# 3. Rodar o app
streamlit run app.py
```
