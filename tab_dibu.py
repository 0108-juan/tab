import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configuración de la página
st.set_page_config(
    page_title="Tablero de Dibujo Digital",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
        font-weight: 700;
        padding: 1rem;
    }
    .section-container {
        background: #f8fafc;
        border-radius: 15px;
        padding: 0;
        margin: 1rem 0;
        border: 2px solid #e2e8f0;
    }
    .section-title {
        background: #1f77b4;
        color: white;
        padding: 1rem 2rem;
        border-radius: 15px 15px 0 0;
        margin: 0;
        font-size: 1.2rem;
        font-weight: 600;
    }
    .section-content {
        background: white;
        padding: 1.5rem;
        border-radius: 0 0 15px 15px;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown('<h1 class="main-header">🎨 Tablero de Dibujo Digital</h1>', unsafe_allow_html=True)

# Layout principal
col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">⚙️ Panel de Control</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">', unsafe_allow_html=True)
    
    # Controles
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300)
    
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point")
    )
    
    stroke_width = st.slider('Grosor de línea', 1, 30, 5)
    stroke_color = st.color_picker("Color de trazo", "#000000")
    bg_color = st.color_picker("Color de fondo", "#FFFFFF")
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎨 Área de Dibujo</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">', unsafe_allow_html=True)
    
    # Canvas
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key="canvas"
    )
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
