from modules.loader import load_documents_from_folder, split_documents
from modules.vector_store import init_pinecone
from langchain_community.embeddings import OpenAIEmbeddings
import os
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec


init_pinecone()
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX_NAME)

docs = load_documents_from_folder("data")
splits = split_documents(docs)

print(f"Generando embeddings para {len(splits)} fragmentos...")
embeddings_model = OpenAIEmbeddings()
texts = [doc.page_content for doc in splits]
metadatas = [{"text": doc.page_content} for doc in splits]
vectors = embeddings_model.embed_documents(texts)

ids = [f"doc-{i}" for i in range(len(vectors))]
to_upsert = list(zip(ids, vectors, metadatas))

print(f"Insertando {len(to_upsert)} vectores en Pinecone...")
index.upsert(vectors=to_upsert)
print("Ingesta completada con éxito.")
