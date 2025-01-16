# -*- coding: utf-8 -*-
"""
@author: Gerhard

file://../doc

"""


# https://www.datacamp.com/de/tutorial/streamlit


import pandas as pd
import numpy as np
import streamlit as st
import os.path
from config import pathToData

st.set_page_config(page_title = "AviSta") 
st.title("AviSta - Avifauna in Starnberg.")

st.write("## Willkommen!")

st.markdown(
    """
    Auswertungen von avifaunistischen Daten im Landkreis Starnberg.

    ### Woher kommen die Daten?
    - Alle Daten kommen von der Plattform [ornitho.de](https://www.ornitho.de). Es werden Daten aus dem Landkreis Starnberg ausgewertet.
    - Ein Großteil der Daten und die Auswertungen wurden von der [Arbeitsgemeinschaft Starnberger Ornithologen (ASO)](https://starnberg.lbv.de/ornithologie/) erstellt.
"""
)