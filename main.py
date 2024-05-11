import streamlit as st
import os
from langchain.llms import GooglePalm
from dotenv import load_dotenv
load_dotenv()
import translate
from langchain.agents import AgentType, initialize_agent, load_tools

st.info("শমসের নিজেকে আপডেট করতে থাকবে")


st.title("🤓সবজান্তা শমসের🤓 V.0.1")
st.subheader("জিজ্ঞাসা করুন.....")

translating=translate.Translator(to_lang='eng')
question=translating.translate(st.text_input("প্রশ্ন: "))

llm=GooglePalm(google_api_key=os.environ['google_api_key'], temperature=0)



def shobjanta():
    tools=load_tools(['wikipedia', 'llm-math'], llm=llm)
    agent=initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False
    )
    response= agent.run(question)
    translator=translate.Translator(to_lang='bn')
    translated_response=translator.translate(response)
    return translated_response

if question:
    st.subheader("উত্তর: ")
    reply=shobjanta()
    st.write(reply)





    
