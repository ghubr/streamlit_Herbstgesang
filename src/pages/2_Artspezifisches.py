# -*- coding: utf-8 -*-
"""
@author: Gerhard

"""


# https://www.datacamp.com/de/tutorial/streamlit


import pandas as pd
import numpy as np
import streamlit as st
import os.path
from config import pathToData

st.title("Artspezifisches")
st.caption("Ein ASO-Projekt im Landkreis Starnberg")
# st.caption()

tab1, tab2, tab3, tab4 = st.tabs(["Dies", "Das"])
