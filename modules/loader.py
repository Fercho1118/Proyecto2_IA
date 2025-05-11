from pathlib import Path
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents_from_folder(folder="data"):
    docs = []
    for file in Path(folder).glob("*.txt"):
        loader = TextLoader(str(file))
        docs.extend(loader.load())
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=150,
        chunk_overlap=20
    )
    return splitter.split_documents(docs)
