# app.py - Versión que USA chatbot.py
import streamlit as st
from chatbot import ChatbotNutricion

st.set_page_config(page_title="Chatbot Saludable", page_icon="🥗")
st.title("🍏 Asesor de Comida Saludable")

# Inicializar el chatbot (importado de chatbot.py)
if "bot" not in st.session_state:
    st.session_state.bot = ChatbotNutricion()

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "¡Hola! Soy tu asesor nutricional 🥑 ¿En qué puedo ayudarte?"}]

# Mostrar mensajes
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input del usuario
if prompt := st.chat_input("¿Qué quieres saber sobre comida saludable?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("🍏 Consultando a DeepSeek..."):
            respuesta = st.session_state.bot.preguntar(prompt)
        st.markdown(respuesta)
    
    st.session_state.messages.append({"role": "assistant", "content": respuesta})