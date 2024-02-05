## integrate our code OpenAI API

import os
from constants import openai_key
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = openai_key
import streamlit as st


#stream lit framework

st.title("Langchain Example 1 Application")

first_input_prompt = PromptTemplate(
    input_variables = ['name'],
    template = "Tell me about celebrity {name}"
)
llm =OpenAI(temperature=0.8)
chain = LLMChain(llm=llm,prompt=first_input_prompt,verbose=True)

input_text = st.text_input("Search the topic you want : ")
#open ai LLM model interact





if input_text:
    st.write(chain.run(input_text))