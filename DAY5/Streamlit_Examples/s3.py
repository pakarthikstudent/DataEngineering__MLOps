import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')

#st.write(f'Hello {name}')

if name:
   st.write(f'Hello..{name}')


st.slider('Select your age:')
st.slider('Select your port Range:',500,550)
st.slider('Select your X value:',15,100,25)

name = st.text_input('Enter your name:')
age = st.slider('Select your age:',15,100,25)

if name:
   st.write(f'Hello..{name} your age is:{age}')

d={}
d['Name']=['Ram','Tom','Leo']
d['dept']=['sales','HR','QA']
d['City']=['City1','City2','City3']

df = st.selectbox('Choose your data:',d)
df = pd.DataFrame(d)
st.write(df)



