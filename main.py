import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import time
from data import *

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Paradas Mensais",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado com animações
st.markdown("""
    <style>
    /* Animações gerais */
    .stButton, .stSelectbox, .stTextInput {
        transition: all 0.3s ease-in-out;
    }

    /* Animação para containers */
    div.element-container {
        animation: fadeIn 0.5s ease-in;
    }

    /* Animação para gráficos */
    div.stPlotlyChart {
        animation: slideIn 0.7s ease-out;
    }

    /* Animação para tabelas */
    div.stTable {
        animation: slideUp 0.6s ease-out;
    }

    /* Keyframes para as animações */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes slideIn {
        from { 
            transform: translateX(-20px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes slideUp {
        from {
            transform: translateY(20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }

    /* Estilo das tabelas */
    .stTable {
        font-size: 14px;
    }
    th {
        background-color: #4CAF50;
        color: white;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    .stDataFrame {
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título com logo ajustado
with st.container():
    col1, col2 = st.columns([0.75, 0.25])
    with col1:
        st.markdown('<h1 style="font-size: 2.5em; margin-bottom: 0px;">Dashboard de Paradas Mensais</h1>', unsafe_allow_html=True)
    with col2:
        st.image("https://rrlaminas.com.br/wp-content/uploads/2023/06/Fibra-Logo.png", width=200)

# Função para criar animação de carregamento
def load_section():
    with st.spinner('Carregando...'):
        time.sleep(0.3)  # Pequeno delay para efeito visual

# MDF 1 Section
with st.container():
    load_section()
    st.subheader("Gráfico de Impacto por Parada (MDF 1)")
    fig_mdf1 = go.Figure(data=[
        go.Bar(
            x=[item["descricao"].split()[0:3] for item in mdf1_paradas],
            y=[item["impacto"] for item in mdf1_paradas],
            marker_color='rgba(75, 192, 192, 0.6)',
            marker_line_color='rgba(75, 192, 192, 1)',
            marker_line_width=1
        )
    ])
    fig_mdf1.update_layout(
        yaxis_title="Impacto (M³)",
        height=400,
        margin=dict(t=0, b=0, l=0, r=0)
    )
    st.plotly_chart(fig_mdf1, use_container_width=True)

# MDF 2 Section
with st.container():
    load_section()
    st.subheader("Gráfico de Impacto por Parada (MDF 2)")
    fig_mdf2 = go.Figure(data=[
        go.Bar(
            x=[item["descricao"].split()[0:3] for item in mdf2_paradas],
            y=[item["impacto"] for item in mdf2_paradas],
            marker_color='rgba(153, 102, 255, 0.6)',
            marker_line_color='rgba(153, 102, 255, 1)',
            marker_line_width=1
        )
    ])
    fig_mdf2.update_layout(
        yaxis_title="Impacto (M³)",
        height=400,
        margin=dict(t=0, b=0, l=0, r=0)
    )
    st.plotly_chart(fig_mdf2, use_container_width=True)

# Gráfico de Paradas Repetidas
with st.container():
    load_section()
    st.subheader("Gráfico de Paradas Repetidas")
    fig_pie = px.pie(
        values=paradas_repetidas_dados['horas'],
        names=paradas_repetidas_dados['descricao'],
        height=500
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    st.plotly_chart(fig_pie, use_container_width=True)

# Tabelas
col1, col2 = st.columns(2)

with col1:
    load_section()
    st.subheader("Paradas Mensais MDF 1")
    st.table({
        'TEMPO': [item["tempo"] for item in mdf1_paradas],
        'DESCRIÇÃO DOS IMPACTOS': [item["descricao"] for item in mdf1_paradas],
        'IMPACTO': [f"{item['impacto']} M³" for item in mdf1_paradas]
    })

    st.subheader("Paradas Repetidas MDF 1")
    st.table({
        'DESCRIÇÃO': [item["descricao"] for item in mdf1_repetidas],
        'DURAÇÃO': [item["duracao"] for item in mdf1_repetidas]
    })

with col2:
    load_section()
    st.subheader("Paradas Mensais MDF 2")
    st.table({
        'TEMPO': [item["tempo"] for item in mdf2_paradas],
        'DESCRIÇÃO DOS IMPACTOS': [item["descricao"] for item in mdf2_paradas],
        'IMPACTO': [f"{item['impacto']} M³" for item in mdf2_paradas]
    })

    st.subheader("Paradas Repetidas MDF 2")
    st.table({
        'DESCRIÇÃO': [item["descricao"] for item in mdf2_repetidas],
        'DURAÇÃO': [item["duracao"] for item in mdf2_repetidas]
    })