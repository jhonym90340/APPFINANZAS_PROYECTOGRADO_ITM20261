import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# 1. MOTOR DE IA
try:
    sid = SentimentIntensityAnalyzer()


# 2. CONFIGURACIÓN DE PÁGINA
st.set_page_config(page_title="Sentido Financiero PRO", layout="wide")

# --- CSS: DISEÑO VISUAL PROFESIONAL ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; background-color: #F0F4F8; }
    
    .stTabs [data-baseweb="tab-list"] { background-color: #3AB1D6; padding: 10px; border-radius: 15px 15px 0 0; }
    .stTabs [data-baseweb="tab"] { color: white !important; font-weight: 600; font-size: 14px; }
    
    div.stBlock, div[data-testid="stMetric"], .stTextArea textarea, .stNumberInput input, .stTextInput input {
        background: #FFFFFF !important;
        border-radius: 20px !important;
        padding: 25px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
        margin-bottom: 20px;
        border: none !important;


# --- DATOS DE INVESTIGACIÓN (MUESTRA ACADÉMICA) ---
datos_investigacion = {
    'Categoría': ['Deudas', 'Ahorro', 'Gastos Hormiga', 'Seguros'],
    'Frecuencia': [117, 72, 42, 33],
    'Punto_Critico_Promedio': [65, 25, 15, 10]
}
df_inv = pd.DataFrame(datos_investigacion)

st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>SENTIDO FINANCIERO</h1>", unsafe_allow_html=True)

tabs = st.tabs(["INICIO", "BIENESTAR", "CONECTA", "COMPARATIVA", "PLANIFICADOR", "ACCIÓN", "ESTUDIO"])

# --- TAB 1: INICIO ---
with tabs[0]:
    col_t, col_i = st.columns([1, 1])
    with col_t:
        st.markdown("<br>", unsafe_allow_html=True)
        st.header("Gestiona tu bienestar con sentido")
        st.write("""
        Esta plataforma utiliza la **Inteligencia de Datos** para reducir la carga cognitiva 
        y el estrés económico. Compara tu situación financiera actual con promedios críticos 
        identificados en nuestra investigación académica de 264 casos reales. 
        """)
      

# --- TAB 2: BIENESTAR (CON DESCRIPCIÓN) ---
with tabs[1]:
    st.header("Análisis de Bienestar Emocional")
    col_s1, col_s2 = st.columns([1.5, 1])
    with col_s1:
        st.write("""
        **¿Cómo funciona este análisis?**
        Escribe cómo te sientes hoy respecto a tu dinero. Nuestro motor de IA analizará el lenguaje para determinar tu **Carga Cognitiva**. 
        Si el puntaje es negativo, indica que tus preocupaciones financieras están agotando tu energía mental, lo que dificulta la toma de decisiones racionales.
        """)
        sent_txt = st.text_area("Cuéntanos qué tienes en mente...", height=150)
        if st.button("ANALIZAR MI ESTADO"):
            if sent_txt:
                score = sid.polarity_scores(sent_txt)['compound']
                st.session_state['last_score'] = score
                val_abs = abs(score)
                st.subheader(f"Nivel de Energía Emocional: {val_abs:.2f}")
                if score <= -0.05:
                    st.error(f"Interpretación: Tu estado refleja estrés financiero crónico.")
                else:
                    st.success(f"Interpretación: Reflejas control emocional y resiliencia.")
   

# --- TAB 3: CONECTA (CON RETROALIMENTACIÓN) ---
with tabs[2]:
    st.header("Conecta con tu realidad")
    st.markdown("""
    **Descripción de los Datos:**
    Para entender tu salud financiera, procesamos dos variables clave:
    * **Ingresos Mensuales:** El dinero neto que recibes después de impuestos.
    * **Gastos Fijos:** Compromisos que NO puedes evadir (arriendo, servicios, cuotas). 
    * **Índice de Salud:** Relación porcentual entre gastos e ingresos. El límite saludable es el **50%**.
    """)
 

# --- TAB 4: COMPARATIVA (CON RETROALIMENTACIÓN ESTADÍSTICA) ---
with tabs[3]:
    st.header("Análisis de Posición Estadística")
    st.markdown("""
    **Interpretación Académica:**
    Contrastamos tu situación (Línea Azul) contra los **Puntos Críticos** (Barras Grises) obtenidos en el estudio (N=264). 
    Los puntos críticos representan el nivel donde los participantes reportaron niveles de ansiedad clínica.
    """)
 
