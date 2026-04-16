# 🎮 Fallen IA (Professor) - GameCoach AI

O **Fallen IA (Professor)** é um agente inteligente desenvolvido para atuar como um coach de jogos eletrônicos, ajudando jogadores a evoluírem com base em dados, estratégias e no meta atual dos jogos.

O projeto foi construído utilizando conceitos de **IA, prompts estruturados e base de conhecimento (JSON/CSV)**.

---

## 🚀 Objetivo

Criar um agente capaz de:

- Analisar o perfil do jogador
- Identificar pontos fortes e fracos
- Considerar o meta atual dos jogos
- Gerar planos de treino personalizados
- Ajudar na evolução dentro de jogos competitivos

---

## 🧠 Como funciona

O agente utiliza:

- **System Prompt estruturado** (com regras e exemplos)
- **Base de conhecimento local (`data/`)**
- **Leitura de arquivos JSON e CSV**
- **Lógica em Python para contextualização**

Fluxo:

1. Usuário envia uma pergunta
2. Sistema identifica o jogador e o jogo
3. Dados são carregados da pasta `data`
4. O agente gera uma resposta personalizada como coach

---

## 📁 Estrutura do Projeto

```bash
.
├── data/
│   ├── perfil_jogador.json
│   ├── historico_partidas.csv
│   ├── patch_notes.json
│   ├── meta_atual.json
│   ├── planos_treino.json
│   └── estatisticas_jogos.csv
│
├── gamecoach_app.py
├── requirements.txt
└── README.md
```

🗂️ Base de Conhecimento

A pasta data/ contém dados utilizados pelo agente:

- Perfil do jogador
- Histórico de partidas
- Meta atual dos jogos
- Patch notes
- Planos de treino
- Estatísticas

Esses dados permitem respostas mais precisas, contextualizadas e personalizadas.
---

🤖 Prompt do Agente

O agente segue um prompt estruturado com:

- Regras de segurança (não inventar informações)
- Uso de dados reais
- Adaptação ao jogador
- Formato padrão de resposta (diagnóstico, treino, foco)

Também utiliza Few-Shot Prompting para reduzir erros e melhorar consistência.

---

🧪 Avaliação

O agente foi testado com base em:

- Assertividade
- Coerência
- Personalização
- Segurança (anti-alucinação)

Cenários testados:

- Evolução de ranking
- Consulta de meta
- Perguntas fora do escopo
- Falta de contexto

---

🎯 Exemplo de Uso

Entrada:

- Sou Ouro 2 no Valorant, como posso subir de elo?

Saída:

- Diagnóstico do jogador
- Análise do meta
- Pontos de melhoria
- Plano de treino
- Foco para próxima partida

---

⚠️ Limitações
- Não acessa dados em tempo real sem integração externa
- Não substitui coaches profissionais
- Não garante resultados ou subida de ranking
-Não utiliza ou incentiva práticas ilegais (cheats)

---

💡 Diferencial
- Personalização baseada em dados
- Estrutura de resposta profissional
- Fácil expansão para novos jogos
- Integração simples com APIs de IA

---
👨‍💻 Autor

Vitor Freitas
Projeto desenvolvido como laboratório de IA aplicada a jogos.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![AI](https://img.shields.io/badge/AI-GameCoach-purple)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

![Repo Size](https://img.shields.io/github/repo-size/VitorForce/dio-lab-bia-do-futuro)
![Last Commit](https://img.shields.io/github/last-commit/VitorForce/dio-lab-bia-do-futuro)
![Stars](https://img.shields.io/github/stars/VitorForce/dio-lab-bia-do-futuro)
![Forks](https://img.shields.io/github/forks/VitorForce/dio-lab-bia-do-futuro)
