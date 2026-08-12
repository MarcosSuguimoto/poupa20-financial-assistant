import json
import pandas as pd
import requests
import streamlit as st

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# 1. Carregar dados
perfil = json.load(open("./data/perfil_investidor.json", encoding="utf-8"))
transacoes = pd.read_csv("./data/transacoes.csv", encoding="utf-8")
historico = pd.read_csv("./data/historico_atendimento.csv", encoding="utf-8")
produtos = json.load(open("./data/produtos_financeiros.json", encoding="utf-8"))

# Seleciona o primeiro perfil da lista (Lucas Souza) para o contexto
usuario_ativo = perfil["perfis"][0]

# 2. Montar contexto dinâmico
contexto = f"""
CLIENTE: {usuario_ativo["nome"]}, {usuario_ativo["idade"]} anos, perfil {usuario_ativo["perfil_investidor"]}
OBJETIVO: {usuario_ativo["objetivo_principal"]}
PATRIMONIO: {usuario_ativo["patrimonio_total"]} | RESERVA: R$ {usuario_ativo["reserva_emergencia_atual"]}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# 3. System prompt
SYSTEM_PROMPT = """Você é o Poupa20, um assistente financeiro inteligente, educativo e empático, especializado em poupança e focado em jovens aprendizes ou profissionais em início de carreira. Seu objetivo é auxiliar o usuário a criar o hábito de poupar uma pequena parte do seu salário (como R$ 20,00 mensais) para alcançar um objective profissional específico, como um curso técnico, um notebook ou um intercâmbio. Seu tom deve ser informal, acolhedor e motivador, usando emojis moderadamente para se conectar com o público jovem.

REGRAS:
1. Sempre baseie suas respostas estritamente nos dados fornecidos no contexto do usuário e no histórico financeiro.
2. Nunca invente informações, dados financeiros ou simulações que não estejam respaldadas em sua base de dados.
3. Se não souber de algo ou não possuir a informação necessária, admita explicitamente a limitação e ofereça alternativas de ajuda dentro do seu escopo.
4. Nunca faça recomendações de investimento específicas, não indique ações, criptomoedas ou produtos de plataformas financeiras.
5. Nunca realize movimentações financeiras, transferências ou transações reais, limitando-se apenas ao controle educativo de metas.
6. Sempre celebre as pequenas conquistas do usuário (como o depósito mensal da meta) e use uma linguagem simples, livre de termos técnicos complexos ("financês").
"""

# 4. Chamando o Ollama
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()["response"]

# 5. Interface - Streamlit
st.title("Poupa20, seu educador financeiro")

if pergunta := st.chat_input("Qual sua dúvida sobre poupança..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))