# -*- coding: utf-8 -*-
"""dashboard"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
hour_df = pd.read_csv('hour.csv')
day_df = pd.read_csv('day.csv')

# Ubah tipe data 'dteday' menjadi datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Title
st.title('Bike Sharing Dashboard')

# Sidebar filters
st.sidebar.header('Filters')

# Date filter
start_date = st.sidebar.date_input("Start Date", day_df['dteday'].min())
end_date = st.sidebar.date_input("End Date", day_df['dteday'].max())

# Ubah tipe data start_date dan end_date menjadi datetime64[ns]
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter data by date
filtered_day_df = day_df[(day_df['dteday'] >= start_date) & (day_df['dteday'] <= end_date)]
filtered_hour_df = hour_df[(hour_df['dteday'] >= start_date) & (hour_df['dteday'] <= end_date)]

# Visualizations

# Line Chart: Jumlah Penyewaan Harian
st.subheader('Jumlah Penyewaan Harian')
plt.figure(figsize=(12, 6))
plt.plot(filtered_day_df['dteday'], filtered_day_df['cnt'])
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan')
plt.xticks(rotation=45)
st.pyplot(plt)

# Bar Chart: Rata-rata Jumlah Penyewaan Berdasarkan Jenis Cuaca
st.subheader('Rata-rata Jumlah Penyewaan Berdasarkan Jenis Cuaca')
plt.figure(figsize=(10, 6))
sns.barplot(x='weathersit', y='cnt', data=filtered_hour_df)
plt.xlabel('Jenis Cuaca (1: Cerah, 2: Berkabut, 3: Hujan Ringan, 4: Hujan Lebat)')
plt.ylabel('Jumlah Penyewaan')
st.pyplot(plt)

# Heatmap: Pola Penyewaan Sepeda Berdasarkan Hari dan Jam
st.subheader('Pola Penyewaan Sepeda Berdasarkan Hari dan Jam')
weekday_hour_df = filtered_hour_df.groupby(['weekday', 'hr'])['cnt'].mean().reset_index()
weekday_hour_df = weekday_hour_df.pivot_table(values='cnt', index='weekday', columns='hr')  # Gunakan pivot_table()
plt.figure(figsize=(12, 6))
sns.heatmap(weekday_hour_df, cmap='coolwarm')
plt.title('Pola Penyewaan Sepeda Berdasarkan Hari dan Jam')
plt.xlabel('Jam dalam Sehari')
plt.ylabel('Hari dalam Seminggu (0: Minggu, 6: Sabtu)')
st.pyplot(plt)

# Bar Chart: Jumlah Pengguna Kasual vs Terdaftar
st.subheader('Jumlah Pengguna Kasual vs Terdaftar')

# Konversi kolom dteday ke string dengan format YYYY-MM-DD
filtered_day_df['dteday'] = filtered_day_df['dteday'].dt.strftime('%Y-%m-%d')

plt.figure(figsize=(10, 6))
sns.barplot(x='dteday', y='casual', data=filtered_day_df, label='Kasual', color='skyblue')
sns.barplot(x='dteday', y='registered', data=filtered_day_df, label='Terdaftar', color='coral', bottom=filtered_day_df['casual'])
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Pengguna')
plt.xticks(rotation=45)
plt.legend()
st.pyplot(plt)

# Conclusion
st.subheader('Conclusion')
st.write('Dashboard ini menunjukkan pengaruh cuaca dan pola penyewaan sepeda berdasarkan hari dan jam dalam sehari.')
