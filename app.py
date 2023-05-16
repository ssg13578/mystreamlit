import streamlit as st
import numpy as np
import pandas as pd
import matplotlib

st.title("Map")
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4], columns = ['lat', 'lon']
st.map(df)
# x = st.slider('Select a value')
# st.write(x, ' squared is ', x
