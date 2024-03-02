import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

# Load Data
day_df=pd.read_csv("day_clean.csv")
hour_df=pd.read_csv("hour_clean.csv")


############################################################################################################
# Pertanyaan 1
working_day = day_df[day_df['workingday'] == 1]
non_working_day = day_df[day_df['workingday'] == 0]

# Menghitung rata-rata penyewaan pada hari kerja dan hari libur
average_rentals_working_day = working_day['cnt'].mean()
average_rentals_non_working_day = non_working_day['cnt'].mean()

############################################################################################################
# Pertanyaan 2
# Dictionary untuk mapping nama hari dalam seminggu
day_of_week_map = {
    0: 'Minggu',
    1: 'Senin',
    2: 'Selasa',
    3: 'Rabi',
    4: 'Kamis',
    5: 'Jumat',
    6: 'Sabtu'
}
# Angka 0 dan 6 merepresentasikan hari Minggu dan Sabtu karena pada angka 0 dan 6 workingday = 0

# Ubah nilai numerik menjadi nama hari dalam seminggu
day_df['day_of_week'] = day_df['weekday'].map(day_of_week_map)

# Hitung rata-rata jumlah peminjaman sepeda untuk setiap hari dalam seminggu
avg_rentals_per_day = day_df.groupby('day_of_week')['cnt'].mean()

# Urutkan hari dalam seminggu
avg_rentals_per_day = avg_rentals_per_day.reindex(list(day_of_week_map.values()))


############################################################################################################
# Visualisasi Data
st.title('Visualisasi Data Berdasarkan Pertanyaan Bisnis')

# Visualisasi Bar Chart: Perbandingan Rata-rata Penyewaan pada Hari Kerja dan Hari Libur
st.subheader('Perbandingan Rata-rata Penyewaan pada Hari Kerja dan Hari Libur')

plt.figure(figsize=(8, 6))
plt.bar(['Hari Kerja', 'Hari Libur'], [average_rentals_working_day, average_rentals_non_working_day], color=['blue', 'red'])
plt.xlabel('Tipe Hari')
plt.ylabel('Rata-rata Penyewaan')
plt.title('Perbandingan Rata-rata Penyewaan pada Hari Kerja dan Hari Libur')
st.pyplot(plt)

st.write('Rata-rata penyewaan pada hari kerja adalah', (average_rentals_working_day), 'dan rata-rata penyewaan pada hari libur adalah', average_rentals_non_working_day, '. Oleh karena itu hari kerja dan hari libur tidak terlalu memengaruhi jumlah penyewaan sepeda.')

# Visualisasi Line Plot: Perbandingan Jumlah Rata-rata Peminjaman Sepeda per Jam
st.subheader('Perbandingan Jumlah Rata-rata Peminjaman Sepeda per Jam')
plt.figure(figsize=(12, 6))
sns.lineplot(data=hour_df, x='hr', y='cnt', hue='workingday')
plt.legend(['Hari Kerja', 'Hari Libur'])
plt.xlabel('Jam')
plt.ylabel('Jumlah Rata-rata Peminjaman')
plt.title('Perbandingan Jumlah Rata-rata Peminjaman Sepeda per Jam')
st.pyplot(plt)

st.write('Hari kerja dan hari libur mempengaruhi penyewaan sepeda pada jam tertentu, dimana pada hari kerja penyewaan sepeda lebih tinggi pada jam 7-9 dan 16-19, sedangkan pada hari libur penyewaan sepeda lebih tinggi pada jam 10-16.')

# Visualisasi Bar Chart: Rata-rata Jumlah Peminjaman Sepeda per Hari dalam Seminggu
st.subheader('Rata-rata Jumlah Peminjaman Sepeda per Hari dalam Seminggu')
plt.figure(figsize=(10, 6))
avg_rentals_per_day.plot(kind='bar', color='skyblue')
plt.xlabel('Hari dalam Seminggu')
plt.ylabel('Rata-rata Jumlah Peminjaman')
plt.title('Rata-rata Jumlah Peminjaman Sepeda per Hari dalam Seminggu')
plt.xticks(rotation=45)
st.pyplot(plt)

st.write('Berdasarkan hasil analisis data, didapat fakta bahwa peminjaman sepeda paling sering dilakukan pada hari jumat. Lalu didapat fakta juga bahwa hari minggu merupakan hari dengan peminjaman sepeda paling sedikit. Namun perbedaan jumlah peminjaman sepeda pada hari minggu dan hari lainnya tidak terlalu jauh. Oleh karena itu didapatkan konklusi bahwa hari peminjaman tidak terlalu memengaruhi jumlah peminjaman sepeda.')



