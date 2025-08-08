#import streamlit
#streamlit.title('sample ui app')

import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to streamlit learning')

# display message
# -----------------

st.write('This is test message')
st.write('streamlit easy to learn')

df = pd.DataFrame({'pID':[101,102,103],'pName':['pA','pB','pC']})
st.write('Sample DataFrame')
st.write(df) # display dataframe

df1 = pd.DataFrame(np.random.randn(20,3),columns=['A','B','C'])
st.write(df1)


