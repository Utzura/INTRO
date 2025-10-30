import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="🌈 Mi Primera App Multimodal",
    page_icon="🎨",
    layout="centered"
)

st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #E3F2FD, #E1BEE7);
        color: #222;
    }
    .stApp {
        background: linear-gradient(135deg, #EDE7F6 0%, #E1F5FE 100%);
    }
    .stButton>button {
        background-color: #7E57C2;
        color: white;
        border-radius: 10px;
        border: none;
        height: 45px;
        width: 100%;
        font-size: 16px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #5E35B1;
        transform: scale(1.05);
    }
    .stSelectbox, .stTextInput, .stRadio, .stCheckbox {
        font-weight: 500;
    }
    .stSidebar {
        background-color: #F3E5F5;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #4A148C;
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
