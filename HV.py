import streamlit as st
from streamlit_folium import st_folium
import folium

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(
    page_title="Portafolio - Luis Miguel Guerrero",
    page_icon="🗺️",
    layout="wide"
)

# --- BARRA LATERAL (NAVEGACIÓN) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Puedes poner tu foto real aquí
    st.title("Luis Miguel Guerrero")
    st.subheader("Ingeniero Topográfico")
    st.write("📍 Bogotá, Colombia")
    
    st.markdown("---")
    opcion = st.radio("Navegar a:", ["Hoja de Vida", "Visor Geográfico", "Mis Programas"])
    
    st.markdown("---")
    st.caption("Contacto:")
    st.caption("📧 lmiguelguerrero@outlook.com")
    # Nota: Evita poner tu cédula o teléfono personal en la versión pública web por seguridad.

# --- SECCIÓN 1: HOJA DE VIDA ---
if opcion == "Hoja de Vida":
    st.title("Perfil Profesional")
    st.markdown("""
    **Ingeniero Topográfico** con más de diez años de experiencia en SIG, cartografía y análisis territorial. 
    Especialista en levantamientos georreferenciados, delimitación de comunidades étnicas y áreas protegidas.
    Experto en automatización de procesos con **Python** y bases de datos espaciales.
    """)
    
    # Botón de descarga del PDF
    col_dl, col_blank = st.columns([1, 4])
    with col_dl:
        try:
            with open("hoja_vida.pdf", "rb") as pdf_file:
                st.download_button(
                    label="📄 Descargar CV (PDF)",
                    data=pdf_file,
                    file_name="HV_MiguelGuerrero.pdf",
                    mime="application/pdf"
                )
        except FileNotFoundError:
            st.warning("⚠️ Nota: Sube tu archivo 'hoja_vida.pdf' a la carpeta para activar este botón.")

    st.markdown("---")

    # Experiencia
    st.subheader("💼 Experiencia Profesional")
    
    with st.container():
        c1, c2 = st.columns([3, 1])
        c1.markdown("**Unidad de Restitución de Tierras** | *Profesional Topografía y SIG*")
        c2.markdown("📅 *2015-2017 | 2023-2025*")
        st.write("""
        * Análisis territorial de comunidades étnicas y delimitación de áreas protegidas.
        * Desarrollo de geovisor en Python para la Dirección de Asuntos Étnicos.
        * Análisis en medidas cautelares (Pueblo Barí, Chiribiquete, Llanos del Yarí).
        """)
    
    st.divider()
    
    with st.container():
        c1, c2 = st.columns([3, 1])
        c1.markdown("**Agencia Nacional de Tierras** | *Profesional Topografía y SIG*")
        c2.markdown("📅 *2018-2024*")
        st.write("""
        * Actualización de polígonos geográficos oficiales.
        * Automatización con Python para linderos y efemérides (Reducción 80% tiempos).
        * Coordinación delimitación sitio sagrado Jaba Tanawiskaka.
        """)

    st.divider()
    
    # Formación
    st.subheader("🎓 Formación Académica")
    st.write("**Magíster en Ciencias de la Información y las Comunicaciones (Geomática)** | U. Distrital (2025)")
    st.write("**Magíster en Áreas Protegidas** | UCI México (2023)")
    st.write("**Ingeniero Topográfico** | U. Distrital (2009)")
    
    st.markdown("---")
    st.subheader("🛠 Habilidades Técnicas")
    st.markdown("""
    * **SIG:** ArcGIS, QGIS, AutoCAD Map 3D.
    * **Programación:** Python (Pandas, Folium, Tkinter), PostgreSQL/PostGIS.
    * **Campo:** GNSS, Estación Total, Cartografía Social.
    """)

# --- SECCIÓN 2: VISOR GEOGRÁFICO ---
elif opcion == "Visor Geográfico":
    st.title("🗺️ Portafolio Geográfico")
    st.markdown("Muestra interactiva de zonas donde he gestionado proyectos de delimitación y análisis.")

    # Crear mapa base
    m = folium.Map(location=[4.5709, -74.2973], zoom_start=5, tiles="CartoDB positron")

    # Marcador 1: Chiribiquete
    folium.Marker(
        [0.9, -72.7],
        popup="<b>PNAC Chiribiquete</b><br>Análisis pueblos no contactados",
        icon=folium.Icon(color="green", icon="tree-conifer")
    ).add_to(m)

    # Marcador 2: Llanos del Yarí
    folium.Marker(
        [1.5, -73.5],
        popup="<b>Resguardo Llanos del Yarí</b><br>Análisis de deforestación",
        icon=folium.Icon(color="red", icon="warning-sign")
    ).add_to(m)

    # Marcador 3: Bogotá
    folium.Marker(
        [4.6097, -74.0817],
        popup="<b>Bogotá D.C.</b><br>Gestión Catastral y Geodatabases",
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

    # Renderizar mapa
    st_folium(m, width=1200, height=500)
    
    st.info("💡 En una versión avanzada, aquí subiré GeoJSON/KML reales de los polígonos.")

# --- SECCIÓN 3: MIS PROGRAMAS ---
elif opcion == "Mis Programas":
    st.title("💻 Software y Propiedad Intelectual")
    st.write("Herramientas desarrolladas y registradas ante la DNDA.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("VISGEO")
        st.write("*Visor de información geográfica*")
        st.caption("Registro: 13-103-103")
        st.info("Identificación de errores de cabida y linderos en territorios colectivos.")
        # Aquí pondrías el link real cuando lo tengas en GitHub/SourceForge
        st.link_button("Ver Proyecto", "https://github.com/")

    with col2:
        st.subheader("RETELI")
        st.write("*Redacción Técnica de Linderos*")
        st.caption("Registro: 13-103-102")
        st.info("Automatización de redacción de linderos a partir de bases espaciales.")
        st.link_button("Ver Proyecto", "https://github.com/")

    with col3:
        st.subheader("EPHSYNC")
        st.write("*Descarga de Efemérides GNSS*")
        st.caption("Registro: 13-103-101")
        st.info("Análisis de proximidad a estaciones IGAC y descarga automatizada.")
        st.link_button("Ver Proyecto", "https://github.com/")
