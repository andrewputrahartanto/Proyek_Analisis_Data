#Import Library
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(layout="wide")

# Set Title
st.title("Bike Sharing Dashboard")
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Visualisasi 1", 
                                        "Visualisasi 2", 
                                        "Visualisasi 3", 
                                        "Visualisasi 4", 
                                        "Analisis Lanjutan"])

# Load Dataset
day_df = pd.read_csv("https://raw.githubusercontent.com/andrewputrahartanto/Proyek_Analisis_Data/main/data/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/andrewputrahartanto/Proyek_Analisis_Data/main/data/hour.csv")

# Change Data Type
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])

# Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/andrewputrahartanto/Proyek_Analisis_Data/main/Logo%20Bike.png")
    st.sidebar.title("Bike Sharing")
    st.sidebar.markdown("**• Nama: Andrew Putra Hartanto**")
    st.sidebar.markdown(
        "**• Dataset: [Download](https://raw.githubusercontent.com/andrewputrahartanto/Proyek_Analisis_Data/main/dashboard/main_data.csv)**")
    st.sidebar.markdown(
        "**• Github: [Link](https://github.com/andrewputrahartanto/Proyek_Analisis_Data.git)**")
    st.sidebar.markdown(
        "**• Streamlit: [Link](https://andrewputrahartanto.streamlit.app/)**")

# Add content to Tab 1
with tab1:
    st.header("Bagaimana Perbandingan Pengguna Bike Sharing Pada Tahun 2011 dan 2012?")
    tahun_df = day_df.resample("Y", on="dteday").sum()
    tahun_df = tahun_df.reset_index()
    tahun_df["dteday"] = ["2011", "2012"]
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(tahun_df["dteday"], tahun_df["cnt"])
    for i in range(len(tahun_df["dteday"])):
        ax.text(i, tahun_df["cnt"][i],
                str(tahun_df["cnt"][i]),
                ha="center", va="bottom")
    ax.set_title("Perbandingan Pengguna Bike Sharing Tahun 2011 dan 2012")
    ax.set_xlabel("Tahun")
    ax.set_ylabel("Jumlah Bike Sharing")
    ax.grid(axis="x")
    ax.yaxis.set_major_formatter(
    plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))
    st.pyplot(fig)
    st.caption("Kesimpulan: Pada **tahun 2012** terjadi **lonjakan** yang **sangat besar** **dibandingkan** **tahun 2011**. Pengguna bike sharing pada **tahun 2011** sebesar **1.243.103** pengguna sedangkan **tahun 2012** sebesar **2.049.576** pengguna")

# Add content to Tab 2
with tab2:
    st.header("Bagaimana Tren Pengguna Bike Sharing Setiap Bulan?")
    bulan_df = day_df.resample("M", on="dteday").sum()
    bulan_df = bulan_df.reset_index()
    bulan_df["dteday"] = ["Jan 2011", "Feb 2011", "Mar 2011",
                        "Apr 2011", "Mei 2011", "Jun 2011",
                        "Jul 2011", "Agu 2011", "Sep 2011",
                        "Okt 2011", "Nov 2011", "Des 2011",
                        "Jan 2012", "Feb 2012", "Mar 2012",
                        "Apr 2012", "Mei 2012", "Jun 2012",
                        "Jul 2012", "Agu 2012", "Sep 2012",
                        "Okt 2012", "Nov 2012", "Des 2012"]
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(bulan_df["dteday"], bulan_df["cnt"])
    ax.set_title("Tren Pengguna Bike Sharing Setiap Bulan")
    ax.set_xlabel("Bulan")
    ax.set_ylabel("Jumlah Bike Sharing")
    plt.xticks(rotation=90)
    ax.grid(True)
    ax.yaxis.set_major_formatter(
    plt.matplotlib.ticker.StrMethodFormatter("{x:,.0f}"))
    st.pyplot(fig)
    st.caption("Kesimpulan: Tren pengguna bike sharing setiap bulannya pada tahun 2011 dan 2012 cenderung **berfluktuasi**. Tren pengguna bike sharing pada Bulan **Januari 2011** sampai **Juni 2011 meningkat**, sedangkan pada Bulan **Juni 2011** sampai **Desember 2011** cenderung **menurun**. Pada Bulan **Desember 2021** sampai **September 2012** cenderung **meningkat** kembali, namun pada Bulan **September 2012** hingga **Desember 2012** mengalami **penurunan** kembali. **Puncak** pengguna bike sharing terjadi pada Bulan **September 2012**")

# Add content to Tab 3
with tab3:
    st.header("Bagaimana Traffic Pengguna Bike Sharing Setiap Jam?")
    hour_map = {0:'12 am', 1: '01 am', 2: '02 am', 3: '03 am', 4: '04 am',
            5: '05 am', 6: '06 am', 7: '07 am', 8: '08 am', 9: '09 am',
            10: '10 am', 11: '11 am', 12: '12 pm', 13: '01 pm', 14: '02 pm',
            15: '03 pm', 16: '04 pm', 17: '05 pm', 18: '06 pm', 19: '07 pm',
            20: '08 pm', 21: '09 pm', 22: '10 pm', 23: '11 pm'}
    hour_df['hr'] = hour_df['hr'].map(hour_map)
    total_user_by_hour_df = hour_df.groupby(by=["hr"], observed=True).agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
    }).sort_values(by='hr', ascending=False)
    hour_order = ['12 am', '01 am', '02 am', '03 am', '04 am',
            '05 am', '06 am', '07 am', '08 am', '09 am',
            '10 am', '11 am', '12 pm', '01 pm', '02 pm',
            '03 pm', '04 pm', '05 pm', '06 pm', '07 pm',
            '08 pm', '09 pm', '10 pm', '11 pm']
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.despine(fig)
    sns.set(style="whitegrid")
    sns.barplot(data=total_user_by_hour_df, x='cnt', y='hr', orient='h', order=hour_order)

    for i in ax.containers:
        ax.bar_label(i,fontsize=12)

    ax.set_title("Traffic Bike Sharing Setiap Jam", size=16)
    ax.set_xlabel("Jumlah Bike Sharing", size=12)
    ax.set_ylabel("Waktu", size=12)
    st.pyplot(fig)
    st.caption("Kesimpulan: Traffic bike sharing **tertinggi** terjadi pada pukul **05 PM** yaitu sebesar **336.860** pengguna, urutan **kedua** pada pukul **06 PM** yaitu sebesar **309.772** pengguna, dan urutan **ketiga** pada pukul **08 AM** yaitu sebesar **261.001** pengguna. Sedangkan traffic bike sharing **terendah** terjadi pada pukul **04 AM** yaitu sebesar **4.428** pengguna")

# Add content to Tab 4
with tab4:
    st.header("Bagaimana Komposisi Tipe Pengguna Bike Sharing?")
    user_composition_df = hour_df[['casual', 'registered']].sum()
    casreg_pie = hour_df[['casual', 'registered']].sum()
    fig, ax = plt.subplots(figsize=(12,6))
    ax.pie(
        x=casreg_pie,
        labels=('Kasual', 'Terdaftar'),
        colors=('#8DD09F', '#668D3C'),
        autopct='%1.1f%%',
        wedgeprops={'width': 0.4}
    )
    ax.set_title("Komposisi Tipe Pengguna Bike Sharing", size=10)
    st.pyplot(fig)
    st.caption("Kesimpulan: Bike sharing lebih di dominasi oleh pengguna yang telah **terdaftar** yaitu sebesar **81.2%** dan sisanya sebesar **18.8%** oleh pengguna **kasual**")

# Add content to Tab 5
with tab5:
    st.header("Teknik Analisis Lanjutan: ***RFM Analysis***")
    # Menghitung rfm
    current_date = max(hour_df['dteday'])
    rfm_df = hour_df.groupby('registered').agg({
        'dteday': lambda x: (current_date - x.max()).days,  # Rec
        'instant': 'count',  # Fre
        'cnt': 'sum'  # Mon
    }).reset_index()
    # Mengganti nama kolom
    rfm_df.columns = ['registered', 'Recency', 'Frequency', 'Monetary']
    # Menampilkan hasil
    st.write(rfm_df.head())
    st.caption("**RFM Analysis** digunakan untuk memahami dan mengelompokkan pelanggan berdasarkan cara berperilaku dalam hal waktu terakhir bertransaksi, frekuensi transaksi, dan nilai transaksi.")
    st.caption("**Recency (R)**: Menunjukkan seberapa baru pelanggan melakukan transaksi.")
    st.caption("**Frequency (F)**: Mengukur seberapa sering pelanggan bertransaksi dalam suatu periode waktu tertentu.")
    st.caption("**Monetary (M)**: Menunjukkan seberapa banyak uang yang dihabiskan oleh pelanggan dalam periode waktu tertentu.")