# Import libraries
import numpy as np
import pandas as pd
import streamlit as st

# Setting Layout
st.set_page_config(layout="wide")

# Add Title and Tabs
st.title("Proyek Analisis Data: Bike Sharing Dataset")
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10, tab11 = st.tabs(["Pertanyaan 1", 
                                                                              "Pertanyaan 2", 
                                                                              "Pertanyaan 3", 
                                                                              "Pertanyaan 4", 
                                                                              "Pertanyaan 5", 
                                                                              "Pertanyaan 6", 
                                                                              "Pertanyaan 7", 
                                                                              "Pertanyaan 8", 
                                                                              "Pertanyaan 9", 
                                                                              "Pertanyaan 10", 
                                                                              "Pertanyaan 11"])

# Import Dataframe
day_df = pd.read_csv("https://raw.githubusercontent.com/andrewputrahartanto/Proyek_Analisis_Data/main/data/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/andrewputrahartanto/Proyek_Analisis_Data/main/data/hour.csv")

# Change the Data Type of the "dteday" Column 
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Add Content to Tab
with tab1:
    st.header("Bagaimana tren penyewaan sepeda berdasarkan tahun?")