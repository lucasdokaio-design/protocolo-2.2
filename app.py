import streamlit as st
import pandas as pd

st.set_page_config(page_title="Protocolo 2.2 — Inteligência Tática", page_icon="⚽", layout="centered")

st.title("⚽ Protocolo 2.2 — Central de Inteligência de Apostas")
st.markdown("Busque o confronto, analise o cenário automaticamente e descubra o protocolo vencedor e a melhor odd para a Bet365.")
st.markdown("---")

# Base de Dados Interna Inteligente (Simulando o catálogo de partidas e estatísticas reais)
catalogo_jogos = [
    {
        "partida": "Flamengo x Vasco da Gama",
        "liga": "Campeonato Carioca / Brasileirão",
        "mandante": "Flamengo",
        "visitante": "Vasco da Gama",
        "posse_mandante": 68.5,
        "bloco_adversario": "Bloco Baixo",
        "pressao_15min": "Alta",
        "finalizacoes_certas": 8.1,
        "media_faltas": 28.0,
        "media_cartoes": 5.5,
        "odd_mercado": 1.45,
        "mercado_sugerido": "Over 12.5 Finalizações / Handicap -1.0 Mandante"
    },
    {
        "partida": "Palmeiras x Corinthians",
        "liga": "Campeonato Paulista / Brasileirão",
        "mandante": "Palmeiras",
        "visitante": "Corinthians",
        "posse_mandante": 52.0,
        "bloco_adversario": "Bloco Médio",
        "pressao_15min": "Média",
        "finalizacoes_certas": 4.8,
        "media_faltas": 32.5,
        "media_cartoes": 6.8,
        "odd_mercado": 1.62,
        "mercado_sugerido": "Over 6.5 Cartões na Partida / Over 29.5 Faltas"
    },
    {
        "partida": "Real Madrid x Barcelona",
        "liga": "La Liga",
        "mandante": "Real Madrid",
        "visitante": "Barcelona",
        "posse_mandante": 66.0,
        "bloco_adversario": "Bloco Baixo",
        "pressao_15min": "Alta",
        "finalizacoes_certas": 9.0,
        "media_faltas": 24.0,
        "media_cartoes": 5.2,
        "odd_mercado": 1.38,
        "mercado_sugerido": "Over 11.5 Finalizações / Ambos Marcam"
    },
    {
        "partida": "Manchester City x Arsenal",
        "liga": "Premier League",
        "mandante": "Manchester City",
        "visitante": "Arsenal",
        "posse_mandante": 71.0,
        "bloco_adversario": "Bloco Baixo",
        "pressao_15min": "Alta",
        "finalizacoes_certas": 7.8,
        "media_faltas": 21.5,
        "media_cartoes": 3.8,
        "odd_mercado": 1.28,
        "mercado_sugerido": "Over 6.5 Cantos Mandante / Pressão Territorial"
    }
]

# Campo de Busca Inteligente por Nome de Time ou Jogo
st.subheader("🔍 Buscar Confronto ou Equipe")
termo_busca = st.text_input("Digite o nome do time ou partida (ex: Flamengo, Real, Palmeiras):", "").strip().lower()

# Filtra o catálogo com base no que o usuário digitar
if termo_busca:
    jogos_filtrados = [
        j for j in catalogo_jogos 
        if termo_busca in j['mandante'].lower() or 
           termo_busca in j['visitante'].lower() or 
           termo_busca in j['partida'].lower()
    ]
else:
    jogos_filtrados = catalogo_jogos

if not jogos_filtrados:
    st.warning("⚠️ Nenhum jogo encontrado com esse termo na base ativa. Tente buscar por outro time (ex: Flamengo, Palmeiras, Real).")
else:
    # Se achou, monta o seletor apenas com os resultados da busca
    opcoes_nomes = [j['partida'] for j in jogos_filtrados]
    jogo_escolhido_nome = st.selectbox("Selecione o confronto correspondente:", opcoes_nomes)
    
    # Pega os dados do jogo selecionado
    jogo_atual = next(j for j in jogos_filtrados if j['partida'] == jogo_escolhido_nome)
    
    st.markdown("---")
    st.success(f"📌 **Confronto Selecionado:** {jogo_atual['partida']} ({jogo_atual['liga']})")
    
    # Motor de Decisão Automático (Executa o Protocolo sem intervenção manual de sliders)
    posse = jogo_atual['posse_mandante']
    bloco = jogo_atual['bloco_adversario']
    pressao = jogo_atual['pressao_15min']
    finalizacoes = jogo_atual['finalizacoes_certas']
    faltas = jogo_atual['media_faltas']
    cartoes = jogo_atual['media_cartoes']
    
    # Cruzamento de Variáveis da Matriz
    if posse >= 65.0 and bloco == "Bloco Baixo" and pressao == "Alta" and finalizacoes >= 6.5:
        cenario_nome = "Cenário A — Sufoco Territorial e Domínio Ofensivo"
        foco_protocolo = "Foco em Finalizações, Cantos e Handicap de Pressão"
        valido = True
    elif faltas >= 27.0 and cartoes >= 5.0:
        cenario_nome = "Cenário B — Atrito Físico e Jogo Picotado"
        foco_protocolo = "Foco em Cartões, Faltas e Punições Disciplinares"
        valido = True
    else:
        cenario_nome = "Cenário C — Padrão Neutro / Indefinido"
        foco_protocolo = "Sem Alinhamento com os Protocolos de Segurança"
        valido = False

    # Exibição do Diagnóstico Destrinchado
    st.subheader("📊 Raio-X Automatizado do Jogo")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Possessão Mandante Mapeada", value=f"{posse}%")
        st.metric(label="Média de Finalizações", value=finalizacoes)
        st.metric(label="Pressão (15' Iniciais)", value=pressao)
    with col2:
        st.metric(label="Média de Faltas do Jogo", value=faltas)
        st.metric(label="Média de Cartões do Juiz", value=cartoes)
        st.metric(label="Odd Atual na Bet365", value=jogo_atual['odd_mercado'])

    st.markdown("---")
    st.subheader("💡 Veredito e Melhor Estratégia")
    
    st.info(f"🎯 **Cenário Destrinchado:** {cenario_nome}")
    st.warning(f"📈 **Melhor Protocolo a Executar:** {foco_protocolo}\n\n**Mercado Alvo Ideal:** {jogo_atual['mercado_sugerido']}")
    
    # Análise da Cotação / Odd
    if valido:
        if jogo_atual['odd_mercado'] < 1.35:
            st.error("⚠️ **ALERTA DE ODD ESMAGADA (< 1.35):** Valor muito baixo para entrada simples. Recomendado enviar para a Fila de Múltipla de Processo.")
        else:
            st.success("✅ **APROVADO PARA ENTRADA SOLO:** O cenário estável atende rigorosamente ao protocolo. Executar diretamente na Bet365.")
    else:
        st.error("❌ **OPERAÇÃO DESCARTADA:** O confronto não atinge os níveis de assimetria necessários. Ficar de fora.")
