import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from pinecone import Pinecone
from langchain_community.embeddings import OpenAIEmbeddings

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")


def init_pinecone():
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index_list = pc.list_indexes().names()

    if INDEX_NAME not in index_list:
        pc.create_index(
            name=INDEX_NAME,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
        print(f"Índice '{INDEX_NAME}' creado correctamente.")
    else:
        print(f"Índice '{INDEX_NAME}' ya existe.")


def retrieve_context(query):
    embeddings = OpenAIEmbeddings()
    vector = embeddings.embed_query(query)

    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index(INDEX_NAME)

    results = index.query(vector=vector, top_k=3, include_metadata=True)

    context_chunks = [match["metadata"]["text"] for match in results["matches"] if "text" in match["metadata"]]

    return "\n\n".join(context_chunks)