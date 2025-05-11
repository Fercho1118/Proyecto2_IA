# Asistente Técnico de Consulta

Este proyecto implementa un asistente técnico basado en Streamlit que utiliza modelos de lenguaje grande (LLMs) como GPT-4, Pinecone como almacén vectorial y LangChain para facilitar la integración y ejecución de preguntas sobre documentos cargados en el sistema.

## Instrucciones para la ejecución

1. **Requisitos previos**:
   - Tener Python 3.7+ instalado en tu sistema.
   - Tener acceso a las claves de API necesarias para Pinecone y OpenAI. Estas claves deben ser definidas en un archivo `.env`.
   - Tener un ambiente virtual creado.
     - Para crear un entorno virtual utiliza los siguientes comandos:
        ```bash
        python -m venv myenv
        ```
        ```bash
        .\myenv\Scripts\Activate.ps1
        ```
       
2. **Instalar las dependencias**:
   En el directorio raíz del proyecto, instala las dependencias necesarias utilizando `pip`:
   ```bash
   pip install -r requirements.txt

3. **Configurar el archivo `.env`**:
   Crea un archivo `.env` en la raíz del proyecto con las siguientes variables de entorno (asegúrate de obtener las claves API de los servicios correspondientes):

   ```env
   PINECONE_API_KEY=<tu_pinecone_api_key>
   PINECONE_ENV=<tu_pinecone_environment>
   PINECONE_INDEX_NAME=<nombre_del_indice>
   OPENAI_API_KEY=<tu_openai_api_key>
   ```

4. **Cargar los documentos**:
   Antes de ejecutar la aplicación, debes cargar los documentos que deseas procesar. Para hacerlo, ejecuta el script `ingest.py`, que se encargará de cargar los documentos desde la carpeta data/, dividirlos en fragmentos y subirlos a Pinecone:

   ```bash
   python ingest.py
   ```

   Este paso generará los embeddings y los almacenará en el índice de Pinecone. Si el índice no existe, será creado automáticamente.

5. **Ejecutar el asistente**:
   Una vez configurado todo, puedes iniciar el asistente con el siguiente comando:

   ```bash
   streamlit run main.py
   ```

   Esto abrirá una página en tu navegador donde podrás interactuar con el asistente técnico.

## Descripción de los módulos

### `main.py`

Este es el archivo principal que configura la página de Streamlit, carga el modelo de preguntas y respuestas (QA) y maneja la interacción del usuario. Al recibir una pregunta, consulta el contexto utilizando Pinecone y luego genera una respuesta usando el modelo de GPT-4.

### `ingest.py`

Este script se utiliza para cargar documentos desde una carpeta (`data/`), dividirlos en fragmentos y almacenar los vectores generados en Pinecone. Además, crea el índice en Pinecone si no existe.

### `loader.py`

Módulo encargado de cargar los documentos en formato `.txt` desde la carpeta `data/`. Utiliza la librería `langchain` para procesar y cargar los documentos.

### `vector_store.py`

Este módulo se encarga de la interacción con Pinecone. Inicializa el cliente de Pinecone, crea índices y gestiona las búsquedas semánticas de los documentos cargados, proporcionando el contexto relevante para las preguntas del usuario.

### `qa_chain.py`

Este módulo carga el modelo de lenguaje GPT-4 a través de LangChain y genera las respuestas a partir del contexto proporcionado por Pinecone.

### `utils.py`

Este módulo gestiona la carga de las claves de API desde el archivo `.env` utilizando la librería `dotenv`.

## Explicación de lo aprendido al desarrollar el asistente

Durante el desarrollo de este asistente técnico, el equipo (o individualmente) aprendió sobre la integración de varias tecnologías para crear un flujo de trabajo eficiente y funcional:

1. **Integración de Pinecone con LangChain**: Aprendimos cómo usar Pinecone como almacén vectorial para almacenar y consultar vectores generados a partir de los documentos cargados. Pinecone nos permitió hacer búsquedas semánticas rápidas y escalables.

2. **Modelos de Lenguaje Grande (LLMs)**: Tuvimos la oportunidad de trabajar con modelos de lenguaje de OpenAI, como GPT-4, para generar respuestas precisas a preguntas basadas en un contexto cargado desde una base de datos semántica.

3. **Streamlit para la interfaz**: Usamos Streamlit para crear una interfaz interactiva y fácil de usar para que los usuarios pudieran hacer preguntas sobre los documentos y obtener respuestas en tiempo real.

4. **Manejo de estados en Streamlit**: Aprendimos cómo manejar el estado de la sesión en Streamlit para crear un historial de preguntas y respuestas y permitir interacciones continuas sin perder el contexto.

5. **Optimización de la búsqueda semántica**: Descubrimos cómo realizar búsquedas semánticas con Pinecone, ajustando las dimensiones de los embeddings para mejorar la precisión de las respuestas.

---

## 10 Preguntas de prueba con la data actual

1. ¿Qué es un embedding vectorial y cómo se utiliza?
2. ¿Cuál es el propósito de Pinecone en este sistema?
3. ¿Qué es LangChain y cómo facilita la construcción de aplicaciones con LLMs?
4. ¿Cómo funciona la atención multi-cabeza en los modelos Transformer?
5. ¿Qué es el aprendizaje por transferencia y cómo se aplica en modelos como BERT?
6. ¿Qué son los índices ANN y cómo mejoran las búsquedas en bases de datos vectoriales?
7. ¿Cuál es la diferencia entre similitud coseno y distancia euclidiana al comparar embeddings?
8. ¿Cómo funciona el proceso de fine-tuning en modelos preentrenados?
9. ¿Qué es RAG (Retrieval-Augmented Generation) y cómo mejora la generación de respuestas?
10. ¿Cómo se maneja el contexto dentro de LangChain para mantener el estado entre interacciones?
