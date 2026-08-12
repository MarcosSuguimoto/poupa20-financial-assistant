# 💰 Poupa20 — Assistente Virtual de Educação Financeira

O **Poupa20** é um assistente financeiro inteligente, educativo e empático desenvolvido para auxiliar jovens e profissionais em início de carreira a criarem o hábito de poupar. 

A aplicação utiliza um **Modelo de Linguagem Local (LLM)** alimentado com dados contextuais do usuário (perfil, transações, produtos e histórico) para fornecer orientações personalizadas através de uma interface interativa via web.

---

## 🛠️ Tecnologias Utilizadas

* **[Python 3.10+](https://www.python.org/)** — Linguagem principal do projeto
* **[Streamlit](https://streamlit.io/)** — Interface gráfica web simples e interativa
* **[Ollama](https://ollama.com/)** — Execução local de LLMs de código aberto
* **[Pandas](https://pandas.pydata.org/)** — Leitura e manipulação de históricos estruturados (`.csv`)
* **[Requests](https://requests.readthedocs.io/)** — Comunicação via API REST com o servidor do Ollama

---

## 🧠 Arquitetura e Contexto Dinâmico

O assistente adota uma abordagem baseada em injeção de contexto (*In-Context Learning / RAG básico*):

1. **Dados do Cliente:** O sistema carrega dados do perfil (`.json`), histórico de transações (`.csv`), atendimentos anteriores (`.csv`) e catálogo de produtos (`.json`).
2. **System Prompt Rígido:** Define regras comportamentais para o assistente (tom informal, proibição de recomendações diretas de investimentos e foco estrito nos dados fornecidos).
3. **Pipeline do LLM:** Concatena os dados do cliente ao prompt do sistema e envia a requisição para a API local do **Ollama**.

---

## 📂 Estrutura do Repositório

```text
├── data/
│   ├── perfil_investidor.json
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   └── produtos_financeiros.json
├── src/
│   └── app.py
└── README.md
