import chromadb
from llama_index.core import SimpleDirectoryReader,service_context,settings
from llama_index.core import VectorStoreIndex
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.ollama import Ollama
                    ###loading docs
documents = SimpleDirectoryReader("data").load_data()

db  = chromadb.PersistentClient("./chroma")
chromacollection = db.get_or_create_collection("quickstart")

                #### setting embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

Settings.llm = Ollama(model="mistral",request_timeout=120.0)
            
vector_store = ChromaVectorStore(chroma_collection=chromacollection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)


            ###indexed data
index = VectorStoreIndex.from_documents(
    documents,transformations=[SentenceSplitter(chunk_size=512)]
)

                        ###code for query
query = input("ask question about the data saved in your files:")
if query:
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)
