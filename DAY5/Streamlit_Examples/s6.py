import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')

st.checkbox('yes')
st.button('Click Me')
st.radio('Select your option:',['yes','no'])

st.selectbox('select your model:',['gp4.0','gpt5.0','lamma','gamma'])

st.multiselect('Choose a planet:',['Jupyter','Mars','Neptune'])

st.slider('Pick a number:',15,25)

st.select_slider('Select your rate:',['Bad','Good','Excellent'])