import streamlit as st
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

st.title("Upload de Imagem para Narração")
st.markdown("Faça o upload de uma imagem para gerar uma descrição por voz.")

uploaded_file = st.file_uploader("Escolha uma imagem", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    filename = secure_filename(uploaded_file.name)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(uploaded_file, caption="Imagem carregada.", use_column_width=True)
    st.success(f"Arquivo {filename} carregado com sucesso!")
else:
    st.warning("Nenhuma imagem carregada ainda.")
