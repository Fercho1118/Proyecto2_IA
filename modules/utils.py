import os
from dotenv import load_dotenv

def load_keys():
    load_dotenv()
    keys = {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        "PINECONE_API_KEY": os.getenv("PINECONE_API_KEY"),
        "PINECONE_ENV": os.getenv("PINECONE_ENV"),
        "PINECONE_INDEX_NAME": os.getenv("PINECONE_INDEX_NAME")
    }
    return keys