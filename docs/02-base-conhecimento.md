# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo                   | Formato | Utilização no Agente                                                                 |
| ------------------------- | ------- | ------------------------------------------------------------------------------------ |
| `perfil_jogador.json`     | JSON    | Personalizar recomendações com base no nível, ranking, função e objetivos do jogador |
| `historico_partidas.csv`  | CSV     | Analisar o desempenho do jogador e identificar padrões de melhoria                   |
| `planos_treino.json`      | JSON    | Sugerir rotinas de treinamento personalizadas                                        |
| `patch_notes.json`        | JSON    | Fornecer informações sobre atualizações e balanceamentos recentes                    |
| `meta_atual.json`         | JSON    | Identificar o meta atual e estratégias dominantes                                    |
| `estatisticas_jogos.csv`  | CSV     | Apresentar métricas como taxa de vitória, KDA e desempenho geral                     |
| `guia_personagens.json`   | JSON    | Oferecer orientações sobre agentes, campeões e classes                               |
| `equipamentos_armas.json` | JSON    | Recomendar armas, itens e configurações ideais                                       |
| `mapas_estrategias.json`  | JSON    | Fornecer estratégias e posicionamentos em mapas                                      |
| `fontes_oficiais.json`    | JSON    | Referenciar links para notas oficiais e atualizações dos jogos                       |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados mockados foram adaptados para o contexto de jogos eletrônicos, substituindo informações financeiras por dados estratégicos do universo gamer. Foram incluídos perfis de jogadores, histórico de partidas, estatísticas de desempenho, metas competitivos e atualizações recentes dos jogos.

Além disso, os conjuntos de dados foram expandidos para permitir análises mais precisas e personalizadas. Novos campos foram adicionados, como:

- Nome do jogo
- Ranking do jogador
- Função ou classe
- Taxa de vitória
- KDA e métricas de desempenho
- Objetivos do jogador
- Estratégias recomendadas
- Versão do patch e data de atualização

-Essas adaptações garantem respostas mais assertivas, contextualizadas e alinhadas ao cenário competitivo atual.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os arquivos JSON e CSV são armazenados na pasta data e carregados automaticamente no início da sessão do agente. Essas informações são processadas e organizadas para permitir consultas rápidas e eficientes durante a interação com o usuário.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Jogador:
- Nome: Vitor
- Jogo: Valorant
- Ranking: Ouro 2
- Função: Duelista
- Agente Principal: Jett
- Taxa de Vitória: 54%
- KDA Médio: 1.32
- Objetivo: Alcançar o rank Platina
- Horas de Treino Semanais: 10

Histórico Recente de Partidas:
- 10/03/2026: Vitória – KDA 1.45 – Mapa: Ascent
- 12/03/2026: Derrota – KDA 0.98 – Mapa: Haven
- 14/03/2026: Vitória – KDA 1.60 – Mapa: Bind

Meta Atual:
- Patch: 8.05
- Duelistas em Alta: Jett e Raze
- Mapas Favoráveis: Ascent e Haven
- Tendência Estratégica: Execuções rápidas e domínio de espaço

Plano de Treino Recomendado:
- Treino de mira: 20 minutos por dia
- Estudo de posicionamento: 15 minutos
- Revisão de partidas: 2 vezes por semana
- Foco principal: Consistência e controle de recuo
