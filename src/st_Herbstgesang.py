# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 18:08:29 2024

@author: Gerhard
"""


# https://www.datacamp.com/de/tutorial/streamlit


import pandas as pd
import numpy as np
import streamlit as st
import os.path
from config import pathToData

# csv can be found here
#pathToData = r'E:\\daten\\Projekte\\2021-10-15 oval_referenz\\output\\Herbstgesang'

map_months = { i:["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"][i-1] for i in range(1,13) }

# add_selectbox = st.sidebar.selectbox(
#         "Art wählen:",
#         ("Amsel", "Buchfink", "Fitis")
#     )

tab1, tab2, tab3, tab4 = st.tabs(["Meldungen", "Melder", "Arten", "Phänologien"])

imwidth = 600
with tab1:
    st.header("Gesangs-Meldungen pro Jahr")
    df = pd.read_csv(os.path.join(pathToData, "stdat_Meldungen_pro_Jahr.csv")).set_index('DATE_YEAR')
    st.bar_chart(df)
    # st.image(os.path.join(pathToData, "Singsang-Meldungen_pro_Jahr.png"))
    st.text("Gesangs-Meldungen (Meldungen mit 'Gesang' o.ä. im Kommentar) pro Jahr. Das Projekt wurde erstmals 2024 durchgeführt")
    
    df = pd.read_csv(os.path.join(pathToData, "stdat_Meldungen_pro_Monat.csv"))
    st.header("Gesangs-Meldungen pro Monat")
    # make year categorical
    df["DATE_YEAR"] = pd.Categorical(df.DATE_YEAR)#.astype(cat)
    # st.bar_chart(df, x="DATE_MONTH", y="OBSERVATIONS", stack=False)
    st.bar_chart(df, x="DATE_MONTH", y="OBSERVATIONS", color="DATE_YEAR", stack=False)
    # st.image(os.path.join(pathToData, "Singsang-Meldungen_je_Monat.png"))
    st.text("Gesangs-Meldungen je Monat. Gesangs-Kommentare wurden 12/2023 vorgestellt. Das Projekt begann 8/2024.")
    
    
with tab2:
    st.header("Anzahl der Melder mit Gesangs-Meldungen")
    df = pd.read_csv(os.path.join(pathToData, "stdat_Meldungen_pro_Monat.csv"))
    st.header("Gesangs-Meldungen pro Monat")
    # make year categorical
    df["DATE_YEAR"] = pd.Categorical(df.DATE_YEAR)#.astype(cat)
    # st.bar_chart(df, x="DATE_MONTH", y="OBSERVATIONS", stack=False)
    st.bar_chart(df, x="DATE_MONTH", y="OBSERVATIONS", color="DATE_YEAR", stack=False)
    # st.image(os.path.join(pathToData, "Singsang-Meldungen_je_Monat.png"))
    st.text("Melder von Gesangs-Meldungen je Monat. Gesangs-Kommentare wurden 12/2023 vorgestellt. Das Projekt begann 8/2024.")

with tab3:
    st.header("Arten mit Gesangs-Meldungen (Aug-Dez)")
    df = pd.read_csv(os.path.join(pathToData, "stdat_Arten_pro_Jahr.csv"))
    
    # select Aug-Dez
    df = df[df.DATE_MONTH>=8]
    # df['DATE_MONTH'] = df['DATE_MONTH'].map(map_months)
    st.bar_chart(df, x='DATE_MONTH', stack=False)
    
with tab4:
    st.header("Phänologien")
    
    # Read data
    df = pd.read_csv(os.path.join(pathToData, "stdat_Meldungen_je_Art_und_Monat.csv"))
    # df = pd.read_csv(os.path.join(pathToData, "stdat_Phaenologien_der_Arten.csv"))
    species_available = df.TAXON.unique()
    
    species = df.groupby('TAXON').size()
    species = species[species>10].index.to_numpy()
    
    option_art = st.selectbox(
        "Art wählen:",
        species
    )
    st.write("Phänologie der Gesangsmeldungen (Aug-Dez) für", option_art, ".")
    
    if option_art in species_available:
        d = df[df.TAXON==option_art]
        d = d.set_index('DATE_DECADE').reindex(range(1,37), fill_value=0).reset_index()
        st.bar_chart(
            d,
            x = 'DATE_DECADE',
            y = 'OBSERVATIONS'
            )
        
    




# df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],columns=['lat', 'lon'])
# st.map(df)





#st.checkbox('yes')
#st.button('Click')
#st.radio('Pick your taxon',['Amsel','Buchfink'])
#st.selectbox('Art wählen:',['Amsel','Drossel', 'Fink', 'Star'])
#st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])
#st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
#st.slider('Pick a number', 0,50)
#years = st.text_input("Jahr(e) wählen (z.B. 2024, 2024-2025, 2020-2023;2025", "Type Here ...")
