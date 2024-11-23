from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

import os
# from .models import api_key
from .models import api_key


def create_vector_db(file_path, vector_db_path):
    # Thiết lập biến môi trường
    APIKEY = api_key.objects.get(name='openAI').key
    os.environ["OPENAI_API_KEY"] = APIKEY

    # Load data
    text_loader_kwargs = {'autodetect_encoding': True}
    loader = TextLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)

    # Embedding
    embedding_model = OpenAIEmbeddings(model="text-embedding-3-large")

    # Create vector store
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(vector_db_path)
    return db


# create_vector_db(pdf_data_path)