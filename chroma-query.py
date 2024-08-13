from llama_index.core import SimpleDirectoryReader
import chromadb

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.create_collection(name="mental_health_data")
