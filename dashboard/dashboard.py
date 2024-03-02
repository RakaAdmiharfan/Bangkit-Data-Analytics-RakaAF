import pandas as pd
import streamlit as st

# Load Data
day_df = pd.read_csv("day_clean.csv")
hour_df = pd.read_csv("hour_clean.csv")


############################################################################################################
# Pertanyaan 1
# Kita gunakan dataframe day_df karena jika menggunakan hour maka attribute workingday akan terulang 24x pada hari yang sama
hariKerja = day_df[day_df['workingday'] == 1]
hariLibur = day_df[day_df['workingday'] == 0]

# Menghitung rata-rata penyewaan pada hari kerja dan hari libur
rentals_hariKerja = hariKerja['cnt'].mean()
rentals_hariLibur = hariLibur['cnt'].mean()

# Menghitung rata-rata penyewaan per jam pada hari kerja dan hari libur
jam_rental_hariKerja = hour_df[hour_df['workingday'] == 1].groupby('hr').agg({'cnt': 'mean'})
jam_rental_hariLibur = hour_df[hour_df['workingday'] == 0].groupby('hr').agg({'cnt': 'mean'})


############################################################################################################
# Pertanyaan 2
# Dictionary untuk mapping nama hari dalam seminggu
# Dictionary untuk mapping nama hari dalam seminggu
day_name = {
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
day_df['day_of_week'] = day_df['weekday'].map(day_name)

# Hitung rata-rata jumlah peminjaman sepeda untuk setiap hari dalam seminggu
rentals_per_hari = day_df.groupby('day_of_week')['cnt'].mean()

# Urutkan hari dalam seminggu
rentals_per_hari = rentals_per_hari.reindex(list(day_name.values()))


############################################################################################################
# Visualisasi Data
st.write('Nama: Raka Admiharfan Fatihah')
st.write('Email: m002d4ky2495@bangkit.academy')
st.write('ID Dicoding: raka_af')

st.title('Visualisasi Data Berdasarkan Pertanyaan Bisnis')

# Visualisasi Bar Chart: Perbandingan Rata-rata Penyewaan pada Hari Kerja dan Hari Libur
st.subheader('Perbandingan Rata-rata Penyewaan pada Hari Kerja dan Hari Libur')
st.bar_chart({'Hari Kerja': rentals_hariKerja, 'Hari Libur': rentals_hariLibur})

st.write('Rata-rata penyewaan pada hari kerja adalah', round(rentals_hariKerja, 2), 'dan rata-rata penyewaan pada hari libur adalah', round(rentals_hariLibur, 2), '. Oleh karena itu, hari kerja dan hari libur tidak terlalu memengaruhi jumlah penyewaan sepeda.')

# Visualisasi Line Plot: Perbandingan Jumlah Rata-rata Peminjaman Sepeda per Jam
st.subheader('Perbandingan Jumlah Rata-rata Peminjaman Sepeda per Jam')
st.line_chart(jam_rental_hariKerja.rename(columns={'cnt': 'Hari Kerja'}).join(jam_rental_hariLibur.rename(columns={'cnt': 'Hari Libur'})))

st.write('Hari kerja dan hari libur mempengaruhi penyewaan sepeda pada jam tertentu, di mana pada hari kerja penyewaan sepeda lebih tinggi pada jam 7-9 dan 16-19, sedangkan pada hari libur penyewaan sepeda lebih tinggi pada jam 10-16.')

# Visualisasi Bar Chart: Rata-rata Jumlah Peminjaman Sepeda per Hari dalam Seminggu
st.subheader('Rata-rata Jumlah Peminjaman Sepeda per Hari dalam Seminggu')
st.bar_chart(rentals_per_hari)

st.write('Berdasarkan hasil analisis data, ditemukan fakta bahwa peminjaman sepeda paling sering dilakukan pada hari Jumat. Lalu, ditemukan juga bahwa hari Minggu merupakan hari dengan peminjaman sepeda paling sedikit. Namun, perbedaan jumlah peminjaman sepeda pada hari Minggu dan hari lainnya tidak terlalu jauh. Oleh karena itu, dapat disimpulkan bahwa hari peminjaman tidak terlalu memengaruhi jumlah peminjaman sepeda.')