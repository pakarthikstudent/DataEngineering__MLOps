import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')

st.image('C:\\Users\\karth\\OneDrive\\Pictures\\test1.png')
#st.audio('file.mp3')
#st.video('file.mp4')

uploaded_file = st.file_uploader('Select your input file:')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

