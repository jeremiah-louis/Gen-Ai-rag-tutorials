import os
from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    get_response_synthesizer,
    Settings,
)
from llama_index.core.response_synthesizers import ResponseMode
from llama_index.llms.openai import OpenAI
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SimilarityPostprocessor

openai_api_key = os.getenv("OPENAI_API_KEY")
# The settings.llm provides configurations for the large language model
Settings.llm = OpenAI(model="gpt-4o-mini", api_key=openai_api_key, temperature=0.2)

# The directory reader ingests the documents and treates the directory as a singular file returning each page as a document object
# Each document object is then vectorised into vector-embeddings and are stored in a vector store
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)

retriever = VectorIndexRetriever(index=index, similarity_top_k=2)
response_synthesizer = get_response_synthesizer(
    response_mode=ResponseMode.SIMPLE_SUMMARIZE
)

query_engine = RetrieverQueryEngine(
    node_postprocessors=[(SimilarityPostprocessor(similarity_cutoff=0.8))],
    retriever=retriever,
    response_synthesizer=response_synthesizer,
)

response = query_engine.query(
    "What are the potiential benefits of Social Media Use Among Children and Adolescent"
)

print(response)
