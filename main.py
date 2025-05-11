import streamlit as st
from modules.vector_store import init_pinecone, retrieve_context
from modules.qa_chain import load_qa_chain

st.set_page_config(page_title="Asistente Técnico", layout="centered")
st.title("Asistente de Consulta Técnica")

init_pinecone()
qa_chain = load_qa_chain()

if 'history' not in st.session_state:
    st.session_state.history = []

def send_question(user_query):
    context = retrieve_context(user_query)
    result = qa_chain(context=context, question=user_query)

    st.session_state.history.append({"question": user_query, "answer": result['result'], "context": context})

with st.form(key='input_form', clear_on_submit=True):
    user_input = st.text_input("Escribe tu pregunta sobre los documentos cargados:", key='user_input')
    submit_button = st.form_submit_button(label='Enviar')

    if submit_button and user_input:
        send_question(user_input)

for entry in reversed(st.session_state.history):
    st.write(f"**Pregunta:** {entry['question']}")
    st.write(f"**Respuesta:** {entry['answer']}")
    st.markdown("**Contexto utilizado:**")
    st.code(entry['context'])
    st.markdown("---")
