###drag and dropm function in streamlit
import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))







import streamlit as st
file_png = st.file_uploader("Upload a PDF", type=([".pdf"]))

if file_png:
        file_png_bytes = st.file_reader(file_png)
        st.image(file_png_bytes)
        ###################################

        with st.sidebar:
    st.title("chat with your data")
    st.markdown('''
## About
It is a chat bot made using:
- [Streamlit](https://docs.streamlit.io/) for ui
- [Llamaindex](https://docs.llamaindex.ai/en/stable/) for framework
- [RAG](https://huggingface.co/docs/transformers/en/model_doc/rag)
- [Mistral](https://github.com/ollama/ollama) for large language model
''')

#loading data###
####("local:BAAI/bge-small-en-v1.5")