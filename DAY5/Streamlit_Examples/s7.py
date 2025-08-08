import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')

st.number_input('Pick a number:',0,20)
st.text_input('Email:')
st.date_input('Travelling date')

st.time_input('Meeting Time:')

st.text_area('Description:')

st.file_uploader('upload a photo')
st.color_picker('select your favorite color:')
