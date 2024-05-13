from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.ollama import Ollama
from llama_index.readers.file import PDFReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.ollama import Ollama
import chromadb
from llama_index.core import SimpleDirectoryReader,service_context,settings,VectorStoreIndex
from llama_index.readers.file import PDFReader
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.ollama import OllamaEmbedding


##to watch the process
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))



                    ###loading docs
parser = PDFReader()
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader("data", file_extractor=file_extractor).load_data()
                



# bge embedding model
                #### setting embedding model


Settings.embed_model = OllamaEmbedding("mistral","http://localhost:11434")
embeddings = embed_model.get_text_embedding("Hello World!")
print(len(embeddings))
print(embeddings[:5])

Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
Settings.llm = Ollama(model="mistral",request_timeout=200)

index = VectorStoreIndex.from_documents(
    documents,transformations=[SentenceSplitter(chunk_size=512)]
)




query_engine = index.as_query_engine()
response = query_engine.query(input("enter your question:"))
print(response)