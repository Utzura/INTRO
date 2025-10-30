import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="🌈 Mi Primera App Multimodal",
    page_icon="🎨",
    layout="centered"
)

st.markdown("""
    <style>
    /* Fondo general */
    .stApp {
        background-color: #fafafa;
        color: #222;
        font-family: "Segoe UI", Roboto, sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f0f0f5 !important;
        color: #222;
    }

    /* Títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #3f3d56;
        font-weight: 700;
    }

    /* Botones */
    .stButton>button {
        background-color: #6c63ff;
        color: white;
        border-radius: 8px;
        border: none;
        height: 45px;
        width: 100%;
        font-size: 16px;
        font-weight: 600;
        transition: all 0.25s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #5a52e0;
        transform: scale(1.03);
    }

    /* Inputs */
    .stTextInput>div>div>input, .stSelectbox>div>div>select {
        background-color: #fff;
        color: #222;
    }

    /* Tarjetas visuales */
    .stInfo, .stSuccess {
        background-color: #f8f8ff !important;
        color: #333 !important;
        border-left: 5px solid #6c63ff !important;
    }

    </style>
""", unsafe_allow_html=True)

st.title("🎨 Mi Primera App!!")
st.header("💡 En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("✨ Puedo realizar fácilmente **backend** y **frontend** usando *Streamlit*.")

image = Image.open('Interfaces Mult2.png')
st.image(image, caption='🧠 Interfaces multimodales', use_container_width=True)

texto = st.text_input('🗒️ Escribe algo:', 'Este es mi texto')
st.write('📜 El texto escrito es:', texto)

st.subheader("🧩 Usemos 2 Columnas")
col1, col2 = st.columns(2)

with col1:
    st.subheader("1️⃣ Primera Columna")
    st.write("Las **interfaces multimodales** mejoran la experiencia de usuario.")
    resp = st.checkbox('Estoy de acuerdo')
    if resp:
        st.success('✅ ¡Correcto!')

with col2:
    st.subheader("2️⃣ Segunda Columna")
    modo = st.radio(
        "¿Qué modalidad es la principal en tu interfaz?",
        ('Visual', 'Auditiva', 'Táctil')
    )
    if modo == 'Visual':
        st.info('👁️ La vista es fundamental para tu interfaz.')
    elif modo == 'Auditiva':
        st.info('👂 La audición es fundamental para tu interfaz.')
    elif modo == 'Táctil':
        st.info('✋ El tacto es fundamental para tu interfaz.')

st.subheader("🕹️ Uso de Botones")
if st.button('Presiona el botón'):
    st.success('🎉 ¡Gracias por presionar!')
else:
    st.write('🙃 No has presionado aún.')

st.subheader("🎛️ Selectbox")
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

st.write("➡️ La acción es:", set_mod)

with st.sidebar:
    st.header("⚙️ Configuración de modalidad")
    st.markdown("Selecciona tu **modo preferido** de interacción:")
    mod_radio = st.radio(
        "Escoge la modalidad a usar",
        ("Visual", "Auditiva", "Háptica")
    )
    st.write(f"🔧 Modalidad seleccionada: **{mod_radio}**")
