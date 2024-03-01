import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

model_path = "/home/ubuntu/work/dl/models/llama-2-7b-chat.ggmlv3.q8_0.bin"


def getLamaResponse(title, no_words, blog_style):
    
    llm_model = CTransformers(
        model = model_path,
        model_type = 'llama',
        config = {
            'max_new_tokens':256,
            'temperature':0.01
        }
    )
    
    my_template = """
        write a detailed beautiful blog on {blog_style} niche with title {title} within {no_words} words
    """
    
    print(f'{blog_style}      {title}        {no_words}')
    
    prompt = PromptTemplate(input_variables=["blog_style", "title", "no_words"] , template=my_template)
    
    respone = llm_model(prompt.format(blog_style=blog_style, title=title, no_words=no_words))
    return respone



#streamlit app______

st.set_page_config(
    page_title = 'llm blog generator',
    layout='centered',
    initial_sidebar_state='collapsed'
)


st.header('Generate blogs')

title =  st.text_input('enter topic')

col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input('no of words')
    
with col2:
    blog_style = st.text_input('Niche')
    
submit  = st.button('Generate')

if submit:
    st.write(getLamaResponse(title, no_words, blog_style))
    
