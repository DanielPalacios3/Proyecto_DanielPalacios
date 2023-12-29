import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import seaborn as sns

# Cargar datos desde FastAPI
@st.cache
def load_data(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        st.error("Error al cargar datos desde FastAPI")
        return None
    return pd.DataFrame(response.json()['tracks'])

# URL del endpoint FastAPI
FASTAPI_ENDPOINT = "http://fastapi:8000/tracks/"

# Cargar los datos
df = load_data(FASTAPI_ENDPOINT)

def generate_scatter_plot(df, x, y, title):
    return px.scatter(df, x=x, y=y, title=title)

def generate_histogram(df, column, title):
    return px.histogram(df, x=column, title=title)

def generate_heatmap(df, title):
    corr = df.corr()
    fig = px.imshow(corr, title=title)
    return fig

# Función para generar gráficas
def generate_plot(df, x, y, title):
        try:
            fig = px.scatter(df, x=x, y=y, title=title)
            return fig
        except Exception as e:
            st.error(f"Error al generar la gráfica: {e}")
            return None
        

# Interfaz de usuario en Streamlit
if df is None or df.empty:
    st.error("No se pudieron cargar los datos o los datos están vacíos.")
else:
    st.title("Dashboard de Análisis de Pistas de Spotify")

    # Mostrar estadísticas generales
    st.write("Número total de pistas:", df.shape[0])
    st.write("Artistas únicos:", df['artists'].nunique())

    # Gráfica de popularidad
    st.subheader("Popularidad de las Pistas")
    st.plotly_chart(generate_plot(df, x='track_name', y='popularity', title="Popularidad por Pista"))

    # Gráfica de bailabilidad vs energía
    st.subheader("Bailabilidad vs Energía")
    st.plotly_chart(generate_plot(df, x='danceability', y='energy', title="Bailabilidad vs Energía"))


    st.subheader("Distribución de la Duración de las Pistas")
    st.plotly_chart(generate_histogram(df, 'duration_ms', "Histograma de Duración (ms)"))

    # Scatter Plot de Bailabilidad vs Valencia
    st.subheader("Bailabilidad vs Valencia")
    st.plotly_chart(generate_scatter_plot(df, 'danceability', 'valence', "Bailabilidad vs Valencia"))

    # Histograma de Claves Musicales
    st.subheader("Distribución de Claves Musicales")
    st.plotly_chart(generate_histogram(df, 'key', "Histograma de Claves Musicales"))

    # Mapa de Calor de Correlación
    st.subheader("Mapa de Calor de Correlación de Características de Audio")
    st.plotly_chart(generate_heatmap(df[['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo']], "Correlación entre Características de Audio"))

    

