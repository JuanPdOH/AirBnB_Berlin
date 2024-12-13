
# Importar librerías
import streamlit as st
import pandas as pd
import numpy as np
import io


# Configuración de página
st.set_page_config(page_title="Berlín, un posible crecimiento", page_icon=r"\img\puerta_Brand.jpeg", layout="wide", initial_sidebar_state="expanded")

# Inicializar el estado de la aplicación
if 'selected_tab' not in st.session_state:
    st.session_state['selected_tab'] = 'Análisis inicial'

# Funciones para cambiar de pestaña
def go_to_inicio():
    st.session_state['selected_tab'] = 'Inicio'

def go_to_tab2():
    st.session_state['selected_tab'] = 'Cambio de tendencia'

def go_to_powerbi():
    st.session_state['selected_tab'] = 'Gráficos combinados'

def get_df_info(df):
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    return s

# Crear el menú lateral con tres botones
st.sidebar.title("Menú")
st.sidebar.button("Análisis inicial", on_click=go_to_inicio)
st.sidebar.button("Cambio de tendencia", on_click=go_to_tab2)
st.sidebar.button("Gráficos combinados", on_click=go_to_powerbi)

# Crear las tres pestañas
tab1, tab2, tab3 = st.tabs(["Análisis inicial", "Cambio de tendencia", "Gráficos combinados"])

# Contenido de la pestaña "Inicio"
with tab1:
    if st.session_state['selected_tab'] == 'Análisis inicial':
        # Título de la aplicación
        st.markdown("<h1 style='color:skyblue;'>Turismo en Berlín</h1>", unsafe_allow_html=True)
        # Texto con información
        st.write("La industria turística de Berlín sigue recuperándose, pero todavía no está ni cerca del nivel que tenía antes de la pandemia de coronavirus.")
        st.write ("El año pasado, 12,1 millones de huéspedes visitaron la capital y representaron 29,6 millones de pernoctaciones.")
        st.write("Así se desprende de las cifras de la Oficina de Estadística de Berlín-Brandeburgo, que fueron presentadas el viernes por la senadora de Asuntos Económicos, Franziska Giffey (SPD), y el director general de la empresa turística Visit Berlin, Burkhard Kieker.")
        st.write("En 2022, hubo 10,4 millones de huéspedes y 26,5 millones de pernoctaciones.La mayoría de los huéspedes de Berlín son de AlemaniaSin embargo, en el año récord 2019 antes de que comenzara la pandemia, el número de pernoctaciones fue significativamente mayor, con 34,1 millones. No obstante, la proporción de pernoctaciones internacionales el año pasado superó el 40% por primera vez desde 2019.")
        st.write("Sin embargo, la mayoría de los visitantes de Berlín (59,7%) siguen procediendo de Alemania. En cuanto a los visitantes extranjeros, el Reino Unido ocupa el primer lugar con 1,3 millones.")
        st.write("Información obtenida de la web berlin.de, web oficial de Berlín. Publicada el 23 de febrero de 2024")
        # Mostrar imagen
        st.image("F:/Entono_Virtual/Proyecto2/nueva_carpeta/descarga.jpeg", caption="Turismo en Berlín")
        
        #Gráficos analíticos
        st.write("A continuación se presentan los gráficos de la serie de tiempo de la oferta en Berlín de los alojamientos turístico en AirBnB, así como el pronóstico del comportamiento del precio a lo largo del tiempo utilizando un modelo SARIMA.")
        st.image(r"\graphics\sarima1_1.png")
        st.image(r"\graphics\sarima1_2.png")
        st.write("Los datos resultantes demostraban que la mayoría de los coeficientes del modelo no eran significativos, por tanto revisé los datos y su relación.")
        
        
        st.write("En el siguiente gráfico se muestra la serie de tiempo de la oferta de alojamientos turísticos en Berlín en AirBnB, pero filtrando los datos para mostrar el comportamiento de aquellos alojamientos que tuvieran alguna disponibilidad a lo largo del año y medio que tenemos de datos.")
        st.image(r"\graphics\sarima2_1.png")
        st.image(r"\graphics\sarima2_2.png")
        st.write("Este cambio en el modelo tampoco resultó válido para determinar una estructura temporal de los datos.")
        
        st.write("Decido en este momento introducir un cambio significativo en el modelo, introduciendo solo los precios de los alojamientos en el momento en que están disponibles, para ver si se puede captar la temporalidad de los datos.")
        st.image(r"\graphics\sarima3_1.png")
        st.image(r"\graphics\sarima3_2.png")
        st.write("En este caso, los coeficientes del modelo resultaron significativos, por lo que se puede decir que la temporalidad de los datos se ha captado. Pero existe autocorrelación y falta de normalidad en los residuos, por lo que se debe revisar el modelo.")

        st.write("Tras este análisis, se ve que la disponibilidad y los precios parecen decrecer. Por lo tanto se detecta un cambio de tendencia en los alojamientos turísticos que gestiona AirBnB en Berlín.")

# Contenido de la pestaña "Cambio de tendencia"
with tab2:
    if st.session_state['selected_tab'] == 'Cambio de tendencia':
        st.header("Legislación de Berlín con respecto a los alojamientos turísticos")
        # Agrega aquí el contenido de tu segunda pestaña
        st.write("La noticia, de la que se hacía eco medio mundo, queda explicada claramente en el artículo del periodista Ben Knight que publica en su web el 13/03/2024 la DW(Deutsche Welle).")
        st.write("'Sentencia sobre vivienda en Berlín: mala noticia para Airbnb.")
        st.write("Miles de apartamentos vacacionales en Berlín podrían volver pronto al mercado de alquiler debido a una reciente sentencia judicial. Y la UE ha creado una nueva normativa para alquileres de corta duración.")
        st.write("Hasta ahora, dicha ley sólo se aplicaba a las propiedades que se habían convertido en apartamentos de vacaciones después de su entrada en vigor, pero la nueva sentencia aclara que también se puede aplicar a los apartamentos vacacionales que ya existían antes de 2014.")
        st.write("Airbnb no hizo comentarios sobre este fallo judicial, pero en declaraciones anteriores señaló que los propietarios que ofrecen apartamentos en su plataforma están obligados a registrarse, como parte de su iniciativa para el turismo responsable y la protección de la vivienda.'")
        st.write("Estas breves líneas sacadas del artículo, me hicieron valorar los datos del listado de alojamientos turísticos en Berlín de AirBnB y ver si se podía detectar un cambio de tendencia en los datos.")


        st.write("")
        st.write("")
        st.write("A continuación dejo reflejado con la información de la tabla de datos inicial y la final, el necesario tratamiento de los datos para dejar solo aquellos necesarios para el análisis.")
        listings_df = pd.read_csv('https://data.insideairbnb.com/germany/be/berlin/2024-09-18/data/listings.csv.gz', compression='gzip')
        df_limpio99 = pd.read_csv(r'\df_limpio.csv')

        st.header("Información de Listings")
        listings_info = get_df_info(listings_df)
        st.text(listings_info)

        st.header("Información de df_limpio99")
        df_limpio99_info = get_df_info(df_limpio99)
        st.text(df_limpio99_info)

        


    
# Contenido de la pestaña "Gráficos combinados"
with tab3:
    if st.session_state['selected_tab'] == 'Gráficos combinados':
        st.header("Análisis de alternativas")
        powerbi_url = "https://app.powerbi.com/reportEmbed?reportId=16af6fa6-f508-4dea-b627-f8240fea217b&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64"
        st.components.v1.iframe(powerbi_url, width=1450, height=875, scrolling=True)

        st.image('F:\entono_virtual\proyecto2\img\distritos-berlin.png', caption="Distritos de Berlín")