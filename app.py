import streamlit as st
from PIL import Image

# Configuración base
st.set_page_config(page_title="Mi Primera App", page_icon="🎨")

# 🌈 Estilo sutil
st.markdown("""
<style>
/* Tipografía moderna y limpia */
html, body, [class*="st-"] {
    font-family: "Poppins", "Segoe UI", sans-serif;
    color: #202020;
}

/* Colores sutilmente más oscuros */
h1, h2, h3, h4, h5, h6 {
    color: #aa1e1e; /* rojo oscuro elegante */
}

/* Botones */
.stButton>button {
    background-color: #d62828; /* rojo original */
    color: white;
    border: none;
    border-radius: 6px;
    transition: 0.2s ease-in-out;
}
.stButton>button:hover {
    background-color: #9b1c1c; /* rojo oscuro al pasar el mouse */
}

/* Checkboxes y radios */
.stCheckbox>div, .stRadio>div {
    accent-color: #b71d1d !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    border-color: #b71d1d !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f8f8f8 !important;
}

/* Inputs */
input, textarea {
    border-radius: 6px !important;
    border-color: #ccc !important;
}
</style>
""", unsafe_allow_html=True)

# ------------------- APP -------------------

st.title("🎨 Mi Primera App!!")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Fácilmente puedo realizar backend y frontend.")

image = Image.open('Interfaces Mult2.png')
st.image(image, caption='Interfaces multimodales')

texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write('El texto escrito es:', texto)

st.subheader("Ahora usemos 2 Columnas")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario.")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
        st.write('✅ ¡Correcto!')

with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("¿Qué modalidad es la principal en tu interfaz?", ('Visual', 'Auditiva', 'Táctil'))
    if modo == 'Visual':
        st.write('👁️ La vista es fundamental para tu interfaz.')
    elif modo == 'Auditiva':
        st.write('👂 La audición es fundamental para tu interfaz.')
    elif modo == 'Táctil':
        st.write('✋ El tacto es fundamental para tu interfaz.')

st.subheader("Uso de Botones")
if st.button('Presiona el botón'):
    st.write('🎉 ¡Gracias por presionar!')
else:
    st.write('🙃 No has presionado aún.')

st.subheader("Selectbox")
in_mod = st.selectbox(
    "Selecciona la modalidad",
    ("Audio", "Visual", "Háptico")
)

if in_mod == "Audio":
    set_mod = "🎵 Reproducir audio"
elif in_mod == "Visual":
    set_mod = "🎥 Reproducir video"
elif in_mod == "Háptico":
    set_mod = "🔔 Activar vibración"

st.write("La acción es:", set_mod)

with st.sidebar:
    st.subheader("⚙️ Configura la modalidad")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica")
    )
    st.write("🔧 Modalidad seleccionada:", mod_radio)
