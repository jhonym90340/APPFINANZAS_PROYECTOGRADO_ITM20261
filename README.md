# Sentido Financiero - Proyecto de Grado ITM 2026-1 - INGENIERIA DE SISTEMAS

"El proyecto está desarrollado en Python 3.10, utilizando Streamlit para la interfaz de usuario. El análisis de datos se realizó con Pandas y la inteligencia artificial se implementó mediante NLTK para el análisis de sentimiento (VADER) y Scikit-learn para la extracción de relevancia temática mediante el algoritmo TF-IDF.

Esta metodología se basa en la investigación de Jinfei Zhu, de la Universidad de Chicago (Estados Unidos), quien en 2022 validó estos modelos para identificar las principales preocupaciones financieras a través de datos de Reddit."

"Si bien el modelo base se apoya en la investigación de Jinfei Zhu (University of Chicago), nuestro aporte principal consiste en la transición de la teoría a la práctica mediante el desarrollo de un software interactivo.

Mientras que el estudio original es un análisis estadístico estático de datos históricos, este proyecto escala dicha ciencia hacia una herramienta de gestión financiera preventiva. He diseñado una interfaz que traduce métricas complejas de NLP y carga cognitiva en indicadores visuales simples, permitiendo que un usuario común, sin conocimientos en finanzas o programación, pueda autoevaluar su bienestar emocional y económico en tiempo real."

Como ejecutarlo:

Plataforma interactiva diseñada para la gestión del bienestar económico y la reducción de la Carga Cognitiva. Este sistema integra Inteligencia Artificial para analizar el impacto emocional de las finanzas personales.

 Características Principales
Análisis de Bienestar: Uso de IA (NLP) para detectar niveles de estrés financiero.
Cálculo de Salud: Evaluación heurística basada en ingresos y gastos fijos.
Planificador: Medición de impacto de gastos en la estabilidad emocional.
Evidencia Social: Explorador de datos históricos de Reddit (Crisis 2009).

 Requisitos Previos
Asegúrate de tener instalado:
Python 3.10 o superior
  Git

 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1. Clonar el repositorio:
   
   git clone [https://github.com/JHONYM90340/APPFINANZAS_PROYECTOGRADO_ITM20261.git](https://github.com/JHONYM90340/APPFINANZAS_PROYECTOGRADO_ITM20261.git)
   cd APPFINANZAS_PROYECTOGRADO_ITM20261


2. Crear un entorno virtual (Recomendado):

Bash
python -m venv venv


3. Activar el entorno virtual:

En Windows (PowerShell):

Bash
.\venv\Scripts\Activate.ps1
En macOS/Linux:

Bash
source venv/bin/activate
Instalar dependencias:

Bash
pip install -r requirements.txt





4. Instalar dependencias:

Bash
pip install -r requirements.txt



5. Ejecución de la App
Para iniciar el servidor local de Streamlit, ejecuta el siguiente comando:

Bash
python -m streamlit run app_ayuda_financiera.py


Una vez ejecutado, la aplicación se abrirá automáticamente en tu navegador en http://localhost:8501.

