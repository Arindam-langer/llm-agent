import chromadb
from llama_index.core import SimpleDirectoryReader,service_context,settings,VectorStoreIndex
from llama_index.readers.file import PDFReader
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.ollama import OllamaEmbedding


#from llama_index.embeddings.mistralai import MistralAIEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.embeddings import resolve_embed_model
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.ollama import Ollama

'''
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))        
'''                    
                    
                    
                    ###loading docs
parser = PDFReader()
file_extractor = {".pdf": parser}
documents = SimpleDirectoryReader("data", file_extractor=file_extractor).load_data()
                
         ###indexed data
index = VectorStoreIndex.from_documents(
    documents,transformations=[SentenceSplitter(chunk_size=512)]
)                
                
                
                #### setting embedding model
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

#Settings.embed_model = OllamaEmbedding("mistral","http://localhost:11434")
embeddings = embed_model.get_text_embedding("Hello World!")
print(len(embeddings))
print(embeddings[:5])



'''###inputing model
Settings.llm = Ollama(model="mistral",request_timeout=100.0)
            
            
            
            
            
            
            ###indexed data
index = VectorStoreIndex.from_documents(
    documents,transformations=[SentenceSplitter(chunk_size=512)]
)

                       
                       
                       
                       
                        ###code for query
query = input("ask question about the data saved in your files:(enter exit to end):")
while query != "exit":
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    print(response)
'''