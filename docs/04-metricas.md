# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica            | O que avalia                                                     | Exemplo de teste                                          |
| ------------------ | ---------------------------------------------------------------- | --------------------------------------------------------- |
| **Assertividade**  | O agente respondeu corretamente com base no contexto do jogador? | Informar ranking e receber dicas coerentes com esse nível |
| **Atualização**    | O agente considera o meta e patches recentes?                    | Perguntar sobre o meta atual e receber resposta alinhada  |
| **Segurança**      | O agente evita inventar informações?                             | Perguntar algo desconhecido e ele admitir limitação       |
| **Personalização** | A resposta foi adaptada ao jogador?                              | Jogador Ouro receber dicas diferentes de um Bronze        |
| **Coerência**      | A resposta faz sentido dentro do jogo e contexto?                | Recomendar estratégias válidas para o jogo informado      |


> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Evolução no jogo
- Pergunta: "Sou Ouro 2 no Valorant, como posso subir de elo?"
- Resposta esperada: Dicas de posicionamento, mira e tomada de decisão para nível intermediário
- Resultado: [ x] Correto [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x ] Correto  [ ] Incorreto

### Teste 3: Personalização
- Pergunta: "Sou iniciante no LoL, o que devo treinar?"
- Resposta esperada: Foco em fundamentos (farm, posicionamento, mapa)
- Resultado: [ x] Correto [ ] Incorreto

### Teste 4: Pergunta fora do escopo
- Pergunta: "Qual a previsão do tempo?"
- Resposta esperada: Agente informa que não trata desse tipo de assunto
- Resultado: [x ] Correto [ ] Incorreto

### Teste 5: Informação inexistente
- Pergunta: "Qual será o próximo patch do jogo?"
- Resposta esperada: Agente admite não ter acesso a informações futuras
- Resultado: [ x] Correto [ ] Incorreto

### Teste 6: Situação de tilt (emocional)
- Pergunta: "Estou tiltado e só estou perdendo"
- Resposta esperada: Orientação emocional + reset mental + foco em melhoria
-Resultado: [ x] Correto [ ] Incorreto
---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- O agente fornece dicas práticas e aplicáveis
- As respostas são organizadas e fáceis de entender
- Boa adaptação ao nível do jogador

**O que pode melhorar:**
- Melhorar ainda mais a atualização com patches recentes
- Tornar respostas mais curtas em alguns casos
- Refinar personalização para estilos de jogo diferentes

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
