import streamlit as st

st.set_page_config(page_title="Pou Planet", page_icon=":potted_plant:")


col1, col2, col3 = st.columns((1,6,1))
with col1:
    st.write("")
with col2:
    st.image('images/1.gif')
with col3:
    st.write("")



st.subheader("Hi, I am Pou :wave:")
st.title("A Potted Plant")

option = st.selectbox('?',('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)
