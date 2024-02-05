## integrate our code OpenAI API

import os
from constants import openai_key
from langchain.llms import OpenAI
os.environ["OPENAI_API_KEY"] = openai_key
import streamlit as st

#stream lit framework

st.title("Langchain Demo with OPENAI API")

input_text = st.text_input("Search the topic you want : ")
#open ai LLM model interact

llm =OpenAI(temperature=0.8)



if input_text:
    st.write(llm(input_text))