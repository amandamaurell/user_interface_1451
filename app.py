import streamlit as st
import random

import numpy as np
import pandas as pd

st.markdown("""# This is a header
## This is a sub header
This is text
- **lists** """)

#streamlit                         1.11.1


@st.cache_data
def get_data_cached():
    df = pd.DataFrame({
        'cached column': random.sample(range(1, 100),10),
        'second column': np.arange(10, 101, 10)
    })
    return df

def get_data_random():
    df = pd.DataFrame({
        'random column': random.sample(range(1, 100),10),
        'second column': np.arange(10, 101, 10)
    })
    return df

# this slider allows the user to select a number of lines
# to display in the dataframe
# the selected value is returned by st.slider
line_count = st.slider('Select a line count', 1, 10, 3)

# and used to select the displayed lines
head_df_cached = get_data_cached().head(line_count)

head_df_random = get_data_random().head(line_count)

col1, col2 = st.columns(2)

with col1:
    st.header('Cached DF')
    st.write(head_df_cached)

with col2:
    st.header('Random DF')
    head_df_random
