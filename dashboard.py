# -*- coding: utf-8 -*-
"""dashboard"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
hour_df = pd.read_csv('hour.csv')
day_df = pd.read_csv('day.csv')

# Title
st.title('Bike Sharing Dashboard')

# Sidebar filters
st.sidebar.header('Filters')
selected_season = st.sidebar.selectbox('Season', hour_df['season'].unique())
selected_weekday = st.sidebar.selectbox('Weekday', hour_df['weekday'].unique())
selected_weathersit = st.sidebar.selectbox('Weathersit', hour_df['weathersit'].unique())

# Filter data
filtered_hour_df = hour_df[(hour_df['season'] == selected_season) &
                              (hour_df['weekday'] == selected_weekday) &
                              (hour_df['weathersit'] == selected_weathersit)]

# Visualizations
st.subheader('Pengaruh Cuaca Terhadap Jumlah Penyewaan')
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=filtered_hour_df)
plt.xlabel('Jenis Cuaca (1: Cerah, 2: Berkabut, 3: Hujan Ringan, 4: Hujan Lebat)')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

st.subheader('Pola Penyewaan Sepeda Berdasarkan Jam')
plt.figure(figsize=(10, 6))
sns.lineplot(x='hr', y='cnt', data=filtered_hour_df)
plt.xlabel('Jam dalam Sehari')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Conclusion
st.subheader('Conclusion')
st.write('Dashboard ini menunjukkan pengaruh cuaca dan pola penyewaan sepeda berdasarkan jam dalam sehari.')
