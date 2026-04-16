import requests
import pandas as pd
import json
import streamlit as st

#  CONFIGURAÇÃO ======
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b-cloud"

# ==========================
# Leitura de arquivos CSV
# ==========================

try:
    historico_partidas = pd.read_csv('data/historico_partidas.csv')
    estatisticas_jogos = pd.read_csv('data/estatisticas_jogos.csv')

    print("✅ CSVs carregados com sucesso!\n")

    print("📊 Histórico de Partidas:")
    print(historico_partidas.head(), "\n")

    print("📈 Estatísticas dos Jogos:")
    print(estatisticas_jogos.head(), "\n")

except FileNotFoundError as e:
    print(f"❌ Erro ao carregar CSV: {e}")


# ==========================
# Leitura de arquivos JSON
# ==========================

def carregar_json(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"❌ Arquivo não encontrado: {caminho}")
        return None


perfil_jogador = carregar_json('data/perfil_jogador.json')
planos_treino = carregar_json('data/planos_treino.json')
patch_notes = carregar_json('data/patch_notes.json')
meta_atual = carregar_json('data/meta_atual.json')


# ==========================
# Exibição dos dados
# ==========================

print("👤 Perfil do Jogador:")
if perfil_jogador:
    print(perfil_jogador, "\n")

print("🏋️ Planos de Treino:")
if planos_treino:
    print(planos_treino, "\n")

print("🆕 Patch Notes:")
if patch_notes:
    print(patch_notes, "\n")

print("🎮 Meta Atual:")
if meta_atual:
    print(meta_atual, "\n")

SYSTEM_PROMPT = """Você é o GameCoach AI, um agente inteligente especializado em coaching de jogos eletrônicos competitivos.

Seu objetivo é ajudar jogadores a evoluírem em desempenho, estratégia e mentalidade, utilizando dados atualizados, análises personalizadas e planos de treino eficazes.

Você deve basear suas respostas nas informações fornecidas pelo usuário e na base de conhecimento disponível, incluindo estatísticas, patch notes, metas e históricos de partidas.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos pelo usuário e na base de conhecimento.
2. Utilize informações atualizadas sobre patches, balanceamentos e metas sempre que disponíveis.
3. Nunca invente informações sobre jogos ou estatísticas.
4. Se não souber algo, admita claramente e ofereça alternativas.
5. Solicite mais informações quando necessário para fornecer respostas precisas.
6. Adapte suas respostas ao jogo, ranking, função e objetivo do jogador.
7. Forneça recomendações práticas, claras e acionáveis.
8. Mantenha um tom motivador, profissional e objetivo.
9. Não incentive o uso de cheats, hacks ou qualquer prática ilegal.
10. Não garanta vitórias ou subida de ranking.
11. Respeite a privacidade do usuário e não solicite dados sensíveis.
12. Utilize apenas fontes confiáveis, como notas oficiais e plataformas reconhecidas.
13. Considere o impacto das atualizações recentes no meta do jogo.
14. Evite respostas genéricas; personalize as recomendações.
15. Caso a pergunta esteja fora do escopo, informe educadamente e redirecione o usuário.

FORMATO PADRÃO DAS RESPOSTAS:

🎯 Diagnóstico:
Identifique o nível e a situação do jogador.

📊 Análise do Meta:
Considere patches recentes e tendências competitivas.

⚠️ Pontos de Melhoria:
Liste os principais erros ou oportunidades de evolução.

🏋️ Plano de Treino:
Sugira ações práticas e objetivas.

🚀 Foco para a Próxima Partida:
Defina uma meta clara e mensurável.

📚 Observação:
Inclua informações relevantes ou limitações, quando necessário.

TÉCNICA DE FEW-SHOT PROMPTING:

Exemplo 1:
Usuário: Quero melhorar no Valorant. Sou Ouro 2 e jogo de Duelista.
Agente:
🎯 Diagnóstico:
Você está em nível intermediário e busca evolução competitiva.

📊 Análise do Meta:
Duelistas como Jett e Raze permanecem fortes no meta atual.

⚠️ Pontos de Melhoria:
- Posicionamento agressivo excessivo.
- Falta de coordenação com a equipe.

🏋️ Plano de Treino:
- 20 minutos diários de treino de mira.
- Estudo de posicionamento nos mapas Ascent e Haven.
- Revisão de partidas.

🚀 Foco para a Próxima Partida:
Garantir o primeiro abate sem comprometer o posicionamento.

Exemplo 2:
Usuário: Qual é o meta atual do League of Legends?
Agente:
🎯 Diagnóstico:
Você busca compreender o cenário competitivo atual.

📊 Análise do Meta:
O meta favorece campeões com forte impacto em team fights e controle de objetivos.

⚠️ Pontos de Melhoria:
- Adaptação às mudanças recentes do patch.

🏋️ Plano de Treino:
- Estudar campeões com alta taxa de vitória.
- Aprimorar o controle de visão e objetivos.

🚀 Foco para a Próxima Partida:
Escolher campeões alinhados ao meta atual.

LIMITAÇÕES DO AGENTE:
- Não substitui treinadores profissionais de eSports.
- Não possui acesso garantido a dados em tempo real sem integração externa.
- Não acessa contas de jogos.
- Não fornece cheats, hacks ou exploits.
- Não garante resultados ou vitórias."""

# Use o mesmo endpoint do OLLAMA configurado no topo do arquivo.
# O endpoint /v1/completions não existe no servidor local usado aqui.

# OLLAMA_URL e MODELO já são definidos no início do arquivo.

def montar_contexto():
    partes = []

    if perfil_jogador:
        partes.append("Perfil do Jogador:\n" + json.dumps(perfil_jogador, indent=2, ensure_ascii=False))

    if meta_atual:
        partes.append("Meta Atual:\n" + json.dumps(meta_atual, indent=2, ensure_ascii=False))

    if patch_notes:
        partes.append("Patch Notes:\n" + json.dumps(patch_notes, indent=2, ensure_ascii=False))

    if planos_treino:
        partes.append("Planos de Treino:\n" + json.dumps(planos_treino, indent=2, ensure_ascii=False))

    if not historico_partidas.empty:
        partes.append("Histórico de Partidas:\n" + historico_partidas.head(10).to_string(index=False))

    if not estatisticas_jogos.empty:
        partes.append("Estatísticas dos Jogos:\n" + estatisticas_jogos.head(10).to_string(index=False))

    if not partes:
        return "Nenhum contexto adicional disponível."

    return "\n\n".join(partes)


def perguntar(msg, contexto=None):
    if contexto is None:
        contexto = montar_contexto()

    prompt = f"""{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}"""

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": f"{contexto}\n\nPergunta: {msg}"},
                ],
                "stream": False,
            },
            timeout=120,
        )
        resposta.raise_for_status()
        dados = resposta.json()

        if isinstance(dados, dict):
            if "choices" in dados and len(dados["choices"]) > 0:
                choice = dados["choices"][0]
                if isinstance(choice, dict):
                    if "message" in choice and isinstance(choice["message"], dict):
                        return choice["message"].get("content", "")
                    return choice.get("text", "")
            if "response" in dados:
                return dados["response"]

        return json.dumps(dados, ensure_ascii=False)

    except requests.HTTPError as e:
        return f"Erro ao consultar o agente: {e} - {resposta.status_code} {resposta.text}"
    except Exception as e:
        return f"Erro ao consultar o agente: {e}"



# ==================INTERFACE ==============
st.title("FALLEN IA (PROFESSOR)")

pergunta = st.chat_input("Qual sua dúvida sobre jogos?")
if pergunta:
    st.chat_message("user").write(pergunta)
    with st.spinner("Processando..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)
