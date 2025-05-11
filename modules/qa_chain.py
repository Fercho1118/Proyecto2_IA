from langchain.chat_models import ChatOpenAI

def load_qa_chain():
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)

    def chain(context, question):
        prompt = f"""
        Usa el siguiente contexto para responder la pregunta. Si no sabes la respuesta, responde con "No tengo suficiente información".

        Contexto:
        {context}

        Pregunta:
        {question}
        """
        return {"result": llm.predict(prompt)}

    return chain
