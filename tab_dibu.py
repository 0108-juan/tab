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
        font-size: 3rem !important;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
        background: linear-gradient(45deg, #1f77b4, #2e86ab);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        padding: 1rem;
    }
    .section-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        padding: 0;
        margin: 1rem 0;
        box-shadow: 0 12px 30px rgba(0,0,0,0.15);
        border: 3px solid #e2e8f0;
    }
    .section-title {
        background: linear-gradient(135deg, #4a90e2 0%, #357abd 100%);
        color: white;
        padding: 1.2rem 2rem;
        border-radius: 20px 20px 0 0;
        margin: 0;
        font-size: 1.4rem;
        font-weight: 600;
        border-bottom: 4px solid #2c5282;
        text-align: center;
    }
    .section-content {
        background: white;
        padding: 2rem;
        border-radius: 0 0 20px 20px;
    }
    .control-panel {
        background: #f8fafc;
        border-radius: 15px;
        padding: 1.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .canvas-container {
        border: 4px solid #e2e8f0;
        border-radius: 15px;
        padding: 20px;
        background: #f7fafc;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
    .tool-button {
        background: linear-gradient(45deg, #1f77b4, #2e86ab);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        font-weight: 600;
        transition: all 0.3s ease;
        width: 100%;
        margin: 0.25rem 0;
    }
    .tool-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(31, 119, 180, 0.4);
    }
    .color-preview {
        width: 30px;
        height: 30px;
        border-radius: 50%;
        border: 2px solid #e2e8f0;
        display: inline-block;
        margin-right: 10px;
        vertical-align: middle;
    }
    .dimension-display {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        margin: 1rem 0;
        font-weight: bold;
        border: 2px solid #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown('<h1 class="main-header">🎨 Tablero de Dibujo Digital</h1>', unsafe_allow_html=True)

# Layout principal
col1, col2 = st.columns([1, 1.5])

with col1:
    # Panel de Control
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">⚙️ Panel de Control</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">', unsafe_allow_html=True)
    
    # Dimensiones del tablero
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    st.subheader("📐 Dimensiones del Tablero")
    
    canvas_width = st.slider(
        "**Ancho del tablero**", 
        300, 700, 500, 50,
        help="Ajusta el ancho del área de dibujo"
    )
    
    canvas_height = st.slider(
        "**Alto del tablero**", 
        200, 600, 300, 50,
        help="Ajusta el alto del área de dibujo"
    )
    
    # Mostrar dimensiones actuales
    st.markdown(f"""
    <div class="dimension-display">
        📏 Tamaño actual: {canvas_width} x {canvas_height} px
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Herramientas de dibujo
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    st.subheader("🛠️ Herramientas de Dibujo")
    
    drawing_mode = st.selectbox(
        "**Selecciona la herramienta:**",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
        format_func=lambda x: {
            "freedraw": "✏️ Dibujo Libre",
            "line": "📏 Línea", 
            "rect": "⬜ Rectángulo",
            "circle": "⭕ Círculo",
            "transform": "🔧 Transformar",
            "polygon": "🔷 Polígono",
            "point": "📍 Punto"
        }[x]
    )
    
    stroke_width = st.slider(
        '**Grosor del pincel**', 
        1, 30, 15,
        help="Ajusta el grosor del trazo"
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Colores
    st.markdown('<div class="control-panel">', unsafe_allow_html=True)
    st.subheader("🎨 Paleta de Colores")
    
    col_color1, col_color2 = st.columns(2)
    
    with col_color1:
        stroke_color = st.color_picker(
            "**Color del trazo**", 
            "#000000",
            help="Selecciona el color para dibujar"
        )
        st.markdown(f'<div class="color-preview" style="background-color: {stroke_color};"></div><span>Color de trazo</span>', unsafe_allow_html=True)
    
    with col_color2:
        bg_color = st.color_picker(
            "**Color de fondo**", 
            "#FFFFFF",
            help="Selecciona el color de fondo del tablero"
        )
        st.markdown(f'<div class="color-preview" style="background-color: {bg_color};"></div><span>Color de fondo</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Información de herramientas
    with st.expander("💡 Guía de Herramientas", expanded=True):
        st.markdown("""
        **📝 Herramientas disponibles:**
        - **✏️ Dibujo Libre:** Dibuja libremente
        - **📏 Línea:** Crea líneas rectas
        - **⬜ Rectángulo:** Dibuja rectángulos
        - **⭕ Círculo:** Crea círculos y elipses
        - **🔧 Transformar:** Mueve y escala objetos
        - **🔷 Polígono:** Dibuja polígonos
        - **📍 Punto:** Crea puntos individuales
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)  # Cierre section-content
    st.markdown('</div>', unsafe_allow_html=True)  # Cierre section-container

with col2:
    # Área de Dibujo
    st.markdown('<div class="section-container">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎨 Área de Dibujo</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-content">', unsafe_allow_html=True)
    
    # Información del modo actual
    tool_names = {
        "freedraw": "✏️ Dibujo Libre",
        "line": "📏 Línea", 
        "rect": "⬜ Rectángulo",
        "circle": "⭕ Círculo", 
        "transform": "🔧 Transformar",
        "polygon": "🔷 Polígono",
        "point": "📍 Punto"
    }
    
    st.markdown(f"""
    <div style='background: #e3f2fd; padding: 1rem; border-radius: 10px; margin-bottom: 1rem; border-left: 4px solid #1f77b4;'>
        <strong>Herramienta activa:</strong> {tool_names[drawing_mode]} | 
        <strong>Grosor:</strong> {stroke_width}px | 
        <strong>Color:</strong> <span style='color: {stroke_color};'>■</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Canvas container
    st.markdown('<div class="canvas-container">', unsafe_allow_html=True)
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color=bg_color,
        height=canvas_height,
        width=canvas_width,
        drawing_mode=drawing_mode,
        key=f"canvas_{canvas_width}_{canvas_height}_{drawing_mode}",
        update_streamlit=True
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Acciones adicionales
    col_actions1, col_actions2, col_actions3 = st.columns(3)
    
    with col_actions1:
        if st.button("🔄 Limpiar Tablero", use_container_width=True):
            st.rerun()
    
    with col_actions2:
        if st.button("💾 Guardar Dibujo", use_container_width=True):
            st.success("¡Funcionalidad de guardado lista para implementar!")
    
    with col_actions3:
        if st.button("📤 Exportar", use_container_width=True):
            st.info("¡Funcionalidad de exportación lista para implementar!")
    
    st.markdown('</div>', unsafe_allow_html=True)  # Cierre section-content
    st.markdown('</div>', unsafe_allow_html=True)  # Cierre section-container

# Barra lateral informativa
with st.sidebar:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 15px; color: white; text-align: center;'>
        <h2>🎨</h2>
        <h3>Estudio de Arte Digital</h3>
        <p style='margin: 0; opacity: 0.9;'>Tablero de dibujo interactivo</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: white; padding: 1.5rem; border-radius: 10px; margin: 1rem 0; 
                border: 2px solid #e2e8f0;'>
        <h4 style='color: #2d3748;'>ℹ️ Acerca de</h4>
        <p style='color: #4a5568; font-size: 0.9rem;'>
        Este es un tablero de dibujo digital interactivo con múltiples herramientas 
        y opciones de personalización.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: #f8fafc; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #10B981;'>
        <h4 style='color: #2d3748;'>🚀 Características</h4>
        <ul style='color: #4a5568; font-size: 0.9rem; padding-left: 1.2rem;'>
            <li>7 herramientas de dibujo</li>
            <li>Colores personalizables</li>
            <li>Dimensiones ajustables</li>
            <li>Interfaz responsive</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background: #fff7ed; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #ea580c;'>
        <h4 style='color: #2d3748;'>🎯 Consejos</h4>
        <p style='color: #4a5568; font-size: 0.9rem;'>
        • Usa <strong>Transformar</strong> para mover objetos<br>
        • Ajusta el grosor para diferentes efectos<br>
        • Experimenta con colores y fondos
        </p>
    </div>
    """, unsafe_allow_html=True)

# Información adicional
st.markdown("---")
col_footer1, col_footer2 = st.columns(2)

with col_footer1:
    st.markdown("""
    **🎨 Modo Actual:** {}
    **📏 Dimensiones:** {} x {} px
    **🖌️ Grosor:** {} px
    """.format(
        tool_names[drawing_mode],
        canvas_width,
        canvas_height, 
        stroke_width
    ))

with col_footer2:
    st.markdown("""
    **🌈 Color de Trazo:** <span style='color: {}'>■</span> {}
    **🎨 Color de Fondo:** <span style='color: {}'>■</span> {}
    """.format(
        stroke_color, stroke_color,
        bg_color, bg_color
    ), unsafe_allow_html=True)
