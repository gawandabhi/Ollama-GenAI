import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

#Prompt answer
prompt= ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant. Please response to the question asked"),
        ("user","Question:{question}")
        
    ]
)

#streamlit framework
st.title("Lanchain demo with gemma3")
input_text = st.text_input("what question do you have in your mind?")

#ollama Gemma3 model

llm = Ollama(model="gemma3:1b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))