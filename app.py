#conversation Q& A chatbot
import langchain
import streamlit as st
import os
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

#stream lit UI

st.set_page_config(page_title="Q&A Conversational Bot")
st.header(" Hey lets Chat")

from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(temperature=0.6)

if 'Flowmessage' not in st.session_state:
    st.session_state['Flowmessage'] = [
        SystemMessage(content="You are a helpful assistant just like Jarvis to Tony Stark")
    ]


def get_openai_response(user_question):

    st.session_state['Flowmessage'].append(HumanMessage(content=user_question))
    answer = chat(st.session_state['Flowmessage'])
    st.session_state['Flowmessage'].append(AIMessage(content=answer.content))
    return answer.content
 
input = st.text_input("Input your question:", key="input")
response = get_openai_response(input)

submit = st.button("Submit the question")

if submit:
    st.subheader("The Response is:")
    st.write(response)