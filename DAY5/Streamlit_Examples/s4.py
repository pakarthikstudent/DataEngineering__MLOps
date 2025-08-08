import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')

d={}
d['Name']=['Ram','Tom','Leo']
d['dept']=['sales','HR','QA']
d['City']=['City1','City2','City3']

df = st.selectbox('Choose your data:',d)
df = pd.DataFrame(d)
st.write(df)



