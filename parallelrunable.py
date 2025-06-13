from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel
import streamlit as st
load_dotenv()
st.header("Post Generator")
prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI(model_name="gpt-4", api_key=st.secrets['api_key'], temperature=0)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),
    'linkedin': RunnableSequence(prompt2, model, parser)
})
topic=st.text_input("Enter your topic")
result = parallel_chain.invoke({topic})

if st.button('Create Post'):
    # ✅ Send the final string to the model
 
    st.write(result)

