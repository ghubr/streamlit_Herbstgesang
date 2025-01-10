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


map_months = { i:["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"][i-1] for i in range(1,13) }

# add_selectbox = st.sidebar.selectbox(
#         "Art wählen:",
#         ("Amsel", "Buchfink", "Fitis")
#     )


st.title("Herbstgesang")
st.caption("Ein ASO-Projekt im Landkreis Starnberg")
# st.caption()

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
    
    
    st.header("Gesangs-Meldungen je Art (Aug-Dez) - nur Arten mit min. 10 Meldungen.")
    df = pd.read_csv(os.path.join(pathToData, "stdat_Beobachtungen_pro_Art_und_Jahr.csv"))
   
    df_sum = df.groupby('TAXON')[['OBSERVATIONS']].agg('sum').sort_values(by='OBSERVATIONS', ascending=False).reset_index()
    st.bar_chart(df_sum[df_sum.OBSERVATIONS>=10], x='TAXON', y='OBSERVATIONS', horizontal=True)
    
    df["DATE_YEAR"] = pd.Categorical(df.DATE_YEAR)
    st.bar_chart(df, x='TAXON', y='OBSERVATIONS', color='DATE_YEAR', stack=True, horizontal=True)
    
with tab2:
    st.header("Anzahl der Melder mit Gesangs-Meldungen")
    df = pd.read_csv(os.path.join(pathToData, "stdat_Melder_pro_Monat.csv"))
    # make year categorical
    df["DATE_YEAR"] = pd.Categorical(df.DATE_YEAR)#.astype(cat)
    # st.bar_chart(df, x="DATE_MONTH", y="OBSERVATIONS", stack=False)
    st.bar_chart(df, x="DATE_MONTH", y="MELDER", color="DATE_YEAR", stack=False)
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
    
    obs_count_min = 10
    df = pd.read_csv(os.path.join(pathToData, "stdat_Phaenologien_der_Arten.csv"))
    species = df.groupby('TAXON').GesangOhneA2.sum().sort_values(ascending=False)
    st.dataframe(species, width=600)
    species = species[species>=obs_count_min]
    for tx, d in df.groupby('TAXON'):
        if tx not in species:
            continue
        st.write("Phänologie nice der Gesangsmeldungen für", tx, ".")
        d = df[df.TAXON==tx].drop(columns='TAXON').set_index('DATE_DECADE')
        reorder = {'A2ohneGesang':'4_A2ohneGesang', 'A2mitGesang':'3_A2mitGesang', 'GesangOhneA2':'2_GesangOhneA2', 'wederA2nochGesang':'1_wederA2nochGesang'}
        d = d.rename(columns=reorder)
        st.bar_chart(
            d[reorder.values()],
            #x = 'DATE_DECADE',
            #y = ['A2ohneGesang', 'A2mitGesang', 'GesangOhneA2'],#, 'wederA2nochGesang'],
            color = ['#0000dd', '#dd00dd', '#dd0000', '#dddddd'][::-1],
            stack = True,
            x_label = "Dekade",
            y_label = "Meldungen"
        )


    # Read data
    obs_count_min = 20
    df = pd.read_csv(os.path.join(pathToData, "stdat_Meldungen_je_Art_und_Monat.csv"))
    species_available = df.TAXON.unique()
    
    species = df.groupby('TAXON').OBSERVATIONS.sum().sort_values(ascending=False)
    st.dataframe(species, width=600)
    species = species[species>=obs_count_min]
    for tx, d in df.groupby('TAXON'):
        if tx not in species:
            continue
        st.write("Phänologie der Gesangsmeldungen (Aug-Dez) für", tx, ".")
        d = df[df.TAXON==tx]
        d = d[d.DATE_DECADE>=22] # Aug-Dez
        d = d.set_index('DATE_DECADE').reindex(range(22,37), fill_value=0).reset_index()
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
