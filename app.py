import streamlit as st

st.set_page_config(page_title="Protocolo 2.2", page_icon="⚽", layout="centered")

st.title("⚽ Protocolo 2.2 — Validação Tática ao Vivo")
st.write("Insira os dados da partida em andamento na Bet365 para rodar o protocolo.")
st.markdown("---")

# Identificação da Partida
st.subheader("1. Identificação do Confronto")
col_t1, col_t2 = st.columns(2)
with col_t1:
    mandante = st.text_input("Time Mandante", "Ex: Flamengo")
with col_t2:
    visitante = st.text_input("Time Visitante", "Ex: Vasco")

liga = st.text_input("Campeonato / Liga", "Ex: Brasileirão")

st.markdown("---")
st.subheader("2. Métricas Coletadas (Ao Vivo)")

# Entradas de dados limpas e dinâmicas
col1, col2 = st.columns(2)

with col1:
    posse_mandante = st.slider("Posse de Bola Mandante (%)", 0.0, 100.0, 65.0)
    pressao_15min = st.selectbox("Pressão nos últimos 15min", ["Alta", "Média", "Baixa"])
    finalizacoes = st.number_input("Finalizações Certas (Alvo)", min_value=0.0, max_value=30.0, value=7.0, step=0.5)
    odd = st.number_input("Odd Atual na Bet365", min_value=1.01, max_value=10.0, value=1.45, step=0.01)

with col2:
    bloco_adversario = st.selectbox("Bloco do Visitante", ["Bloco Baixo", "Bloco Médio", "Bloco Alto"])
    media_faltas = st.number_input("Média de Faltas na Partida", min_value=0.0, max_value=50.0, value=25.0, step=0.5)
    media_cartoes = st.number_input("Média de Cartões do Juiz", min_value=0.0, max_value=10.0, value=4.5, step=0.5)
    mercado_alvo = st.text_input("Mercado Alvo Analisado", "Ex: Over 5.5 Cartões / Handicap")

st.markdown("---")
st.subheader("📊 Diagnóstico do Protocolo")

# Motor de Decisão com base nos inputs reais do usuário
if posse_mandante >= 65.0 and bloco_adversario == "Bloco Baixo" and pressao_15min == "Alta" and finalizacoes >= 6.5:
    cenario = "Cenário A (Sufoco Territorial - Foco: Finalizações / Cantos / Handicap)"
    valido = True
elif media_faltas >= 27.0 and media_cartoes >= 5.0:
    cenario = "Cenário B (Atrito Físico - Foco: Cartões / Faltas)"
    valido = True
else:
    cenario = "Cenário C (Fora do Padrão do Protocolo - Sem Valor Tático)"
    valido = False

st.info(f"**Cenário Identificado:** {cenario}")
st.warning(f"**Mercado Alvo:** {mercado_alvo}")
st.metric("Odd Definida", odd)

st.markdown("---")
st.subheader("💡 Veredito para Operação")

if valido:
    if odd < 1.35:
        st.error("⚠️ **ODD ESMAGADA (< 1.35):** Inviável para entrada simples. Enviar para a Fila de Múltipla de Processo.")
    else:
        st.success("✅ **APROVADO PARA ENTRADA SOLO:** Critérios atendidos. Execute manualmente na Bet365.")
else:
    st.error("❌ **DESCARTADO:** O jogo não atinge os parâmetros de segurança do protocolo.")
