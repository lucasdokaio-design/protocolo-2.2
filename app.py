import streamlit as st

st.set_page_config(page_title="Protocolo 2.2", page_icon="⚽", layout="centered")

st.title("⚽ Protocolo 2.2 — Validação Tática")
st.write("Análise direta de cenários e filtragem de cotação para a Bet365.")
st.markdown("---")

# Seleção rápida de jogo
jogo = st.selectbox(
    "Selecione o confronto para análise:",
    [
        "Real Madrid x Getafe (La Liga)",
        "Porto x Sporting (Liga Portugal)",
        "Manchester City x Wolves (Premier League)"
    ]
)

if "Real Madrid" in jogo:
    posse, bloco, pressao, finalizacoes, faltas, cartoes, odd, mercado = 74.0, "Bloco Baixo", "Alta", 8.2, 22.0, 4.1, 1.25, "Over 12.5 Finalizações / Over 6.5 Cantos"
elif "Porto" in jogo:
    posse, bloco, pressao, finalizacoes, faltas, cartoes, odd, mercado = 51.0, "Bloco Médio", "Média", 5.0, 31.5, 6.2, 1.58, "Over 5.5 Cartões / Over 28.5 Faltas"
else:
    posse, bloco, pressao, finalizacoes, faltas, cartoes, odd, mercado = 72.0, "Bloco Baixo", "Alta", 8.5, 20.5, 3.2, 1.42, "Handicap Asiático -1.5 / Over Cantos"

st.markdown("### 📊 Resultado da Matriz")

# Motor do Protocolo
if posse >= 65.0 and bloco == "Bloco Baixo" and pressao == "Alta" and finalizacoes >= 6.5:
    cenario = "Cenário A (Sufoco Territorial - Foco: Finalizações / Cantos)"
    valido = True
elif faltas >= 27.0 and cartoes >= 5.0:
    cenario = "Cenário B (Atrito Físico - Foco: Cartões / Faltas)"
    valido = True
else:
    cenario = "Cenário C (Fora do Padrão - Sem Valor)"
    valido = False

st.info(f"**Cenário:** {cenario}")
st.warning(f"**Mercado Alvo:** {mercado}")
st.metric("Odd Atual na Casa", odd)

st.markdown("### 💡 Veredito de Operação")
if valido:
    if odd < 1.35:
        st.error("⚠️ ODD ESMAGADA (< 1.35): Enviar para Múltipla de Processo.")
    else:
        st.success("✅ APROVADO PARA ENTRADA SOLO: Execute manualmente na Bet365.")
else:
    st.error("❌ DESCARTADO: O jogo não atinge os critérios de segurança.")
