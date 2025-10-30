import streamlit as st
from PIL import Image

st.set_page_config(page_title="Mi Primera App", page_icon="🎨")

# 🎨 Estilo con texto blanco y colores suaves
st.markdown("""
<style>
/* Tipografía moderna */
html, body, [class*="st-"] {
    font-family: "Poppins", "Segoe UI", sans-serif;
    color: #ffffff; /* texto blanco */
    background-color: #101018; /* fondo gris oscuro azulado */
}

/* Títulos vino oscuro */
h1, h2, h3, h4, h5, h6 {
    color: #b52b3a;
}

/* Botones */
.stButton>button {
    background-color: #b52b3a;
    color: white;
    border: none;
    border-radius: 6px;
    transition: 0.2s ease-in-out;
}
.stButton>button:hover {
    background-color: #8c1f2c;
}

/* Checkboxes y radios */
.stCheckbox>div, .stRadio>div {
    accent-color: #b52b3a !important;
    color: white !important;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    border-color: #b52b3a !important;
    color: white !important;
}
div[data-baseweb="select"] span {
    color: white !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #181820 !important;
    color: white !important;
}

/* Inputs */
input, textarea {
    border-radius: 6px !important;
    border-color: #b52b3a !important;
    color: white !important;
    background-color: #2a2a38 !important;
}

/* Texto general */
p, label, span, div {
    color: white !important;
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
