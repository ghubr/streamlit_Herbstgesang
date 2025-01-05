# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:08:29 2024

@author: Gerhard
"""


# https://www.datacamp.com/de/tutorial/streamlit


import streamlit as st




# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Art wählen:",
    ("Amsel", "Buchfink", "Fitis")
)


tab1, tab2, tab3 = st.tabs(["Phänologie", "Year by Year", "Entwclung"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)




st.title ("this is the app title")
st.header("this is the markdown")
st.markdown("this is the header")
st.subheader("this is the subheader")
st.caption("Dog: 22")
st.text("Normaler Text")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')


st.checkbox('yes')
st.button('Click')
st.radio('Pick your taxon',['Amsel','Buchfink'])
st.selectbox('Art wählen:',['Amsel','Drossel', 'Fink', 'Star'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
years = st.text_input("Jahr(e) wählen (z.B. 2024, 2024-2025, 2020-2023;2025", "Type Here ...")

import pandas as pd
df = pd.DataFrame( {'a':[1,2,3], 'b':[0,4,3] })
st.line_chart(df)


import pandas as pd
import numpy as np
import streamlit as st

df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
st.map(df)