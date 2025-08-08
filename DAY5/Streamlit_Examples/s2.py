import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')

df1 = pd.DataFrame(np.random.randn(10,3),columns=['A','B','C'])
st.write('Sample Dataframe')
st.write(df1)
st.line_chart(df1)
