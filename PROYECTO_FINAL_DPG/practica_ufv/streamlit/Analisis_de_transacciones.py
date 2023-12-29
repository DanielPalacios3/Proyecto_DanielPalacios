
import streamlit as st
import time

from pages import dashboard

st.set_page_config(page_title='Spotify Tracks Analysis', layout='wide',     page_icon="🎶")
st.image('Spotify.png')

#placeholder = st.empty()
#with placeholder:
    #from PIL import Image
    #image = Image.open('mired.png')
    #placeholder.image(image, caption='MiRed semantic engine',use_column_width = 'always') 
 #   for seconds in range(5):
  #      placeholder.write(f"⏳ {seconds} Cargando sistema")
   #     time.sleep(1)
#placeholder.empty()


#st.write("# Vamos a ello 👋")

#st.sidebar.success("Selecciona la única página que te voy a dejar seleccionar. Eres libre de seleccionar.")

st.markdown(
    """
Spotify, con su estatus de líder en el mundo del streaming musical, ofrece una extensa biblioteca que refleja la diversidad y riqueza del panorama musical contemporáneo. Este proyecto se centra en analizar de manera exhaustiva el catálogo de Spotify, utilizando una base de datos meticulosamente compilada para explorar no solo la variedad de géneros y artistas, sino también para evaluar detalladamente las propiedades musicales y tendencias de las pistas. El objetivo es proporcionar una herramienta crucial para aquellos interesados en comprender las dinámicas del consumo musical y las preferencias de los usuarios, especialmente desde un punto de vista de análisis de datos y tendencias de mercado.

La base de datos, creada mediante el uso de la API web de Spotify y técnicas de programación en Python, se presenta en formato CSV, facilitando su acceso y análisis. Incluye una gama de información sobre las pistas, clasificándolas no solo por género, artista y álbum, sino también proporcionando datos detallados sobre aspectos como popularidad, duración, y si contienen contenido explícito.

Además, esta base de datos enriquece el análisis con características de audio únicas para cada pista. Esto incluye bailabilidad, energía, tono, volumen, modo, presencia de habla, acústica, e instrumentalidad. Estos elementos permiten evaluar las pistas más allá de su popularidad o género, ofreciendo una comprensión profunda de sus cualidades musicales.

Los atributos adicionales como vivacidad, valencia, tempo y time_signature ofrecen una perspectiva más amplia sobre la experiencia auditiva, permitiendo a los usuarios discernir patrones y tendencias en una variedad de géneros. Este conjunto de datos es una herramienta valiosa para aquellos que buscan hacer elecciones informadas y personalizadas en su experiencia de escucha, y es especialmente útil para científicos de datos y entusiastas de la música que deseen explorar la intersección entre la música y la tecnología.
    
    La práctica os la voy a evaluar del siguiente modo:
    
    1. Para tener un apto (5) deberéis buscar un conjunto de datos, documentarlo, y hacer un dashboard. La nota puede llegar a 6 en función de 
       que lo que me quieras contar se entienda bien con el dashboard que me muestras. 
    2. Para llegar al 7, deberá tener gráficos de tipo interactivos.
    3. Para llegar al 8, en el backend deberá tener un método post, que tenga sentido.
    4. Para llegar al 9, deberás utilizar una jerarquía de clases con BaseModel y, además, hacer una adecuada gestión de errores: excepciones y logs.
    5. Para llegar al 10, deberías utilizar una base de datos en un servicio adicional. 
    6. Me haría muy feliz si utilizaseis un ORM como SQLAlchemy.
   
    A por ello! 💪💪💪
"""
)
