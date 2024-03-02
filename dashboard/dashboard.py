import pandas as pd
import streamlit as st

# Load Data
day_df = pd.read_csv("day_clean.csv")
hour_df = pd.read_csv("hour_clean.csv")


############################################################################################################
# Pertanyaan 1
working_day = day_df[day_df['workingday'] == 1]
non_working_day = day_df[day_df['workingday'] == 0]

# Menghitung rata-rata penyewaan pada hari kerja dan hari libur
average_rentals_working_day = working_day['cnt'].mean()
average_rentals_non_working_day = non_working_day['cnt'].mean()

# Menghitung rata-rata penyewaan per jam pada hari kerja dan hari libur
hourly_rental_wd = hour_df[hour_df['workingday'] == 1].groupby('hr').agg({'cnt': 'mean'})
hourly_rental_nwd = hour_df[hour_df['workingday'] == 0].groupby('hr').agg({'cnt': 'mean'})


############################################################################################################
# Pertanyaan 2
# Dictionary untuk mapping nama hari dalam seminggu
day_of_week_map = {
    0: 'Minggu',
    1: 'Senin',
    2: 'Selasa',
    3: 'Rabu',
    4: 'Kamis',
    5: 'Jumat',
    6: 'Sabtu'
}

# Ubah nilai numerik menjadi nama hari dalam seminggu
day_df['day_of_week'] = day_df['weekday'].map(day_of_week_map)

# Hitung rata-rata jumlah peminjaman sepeda untuk setiap hari dalam seminggu
avg_rentals_per_day = day_df.groupby('day_of_week')['cnt'].mean()

# Urutkan hari dalam seminggu dan dimulai dari hari Senin
avg_rentals_per_day = avg_rentals_per_day.reindex(pd.CategoricalIndex(list(day_of_week_map.values()), ordered=True))


############################################################################################################
# Visualisasi Data
st.title('Visualisasi Data Berdasarkan Pertanyaan Bisnis')

# Visualisasi Bar Chart: Perbandingan Rata-rata Penyewaan pada Hari Kerja dan Hari Libur
st.subheader('Perbandingan Rata-rata Penyewaan pada Hari Kerja dan Hari Libur')
st.bar_chart({'Hari Kerja': average_rentals_working_day, 'Hari Libur': average_rentals_non_working_day})

st.write('Rata-rata penyewaan pada hari kerja adalah', round(average_rentals_working_day, 2), 'dan rata-rata penyewaan pada hari libur adalah', round(average_rentals_non_working_day, 2), '. Oleh karena itu, hari kerja dan hari libur tidak terlalu memengaruhi jumlah penyewaan sepeda.')

# Visualisasi Line Plot: Perbandingan Jumlah Rata-rata Peminjaman Sepeda per Jam
st.subheader('Perbandingan Jumlah Rata-rata Peminjaman Sepeda per Jam')
st.line_chart(hourly_rental_wd.rename(columns={'cnt': 'Hari Kerja'}).join(hourly_rental_nwd.rename(columns={'cnt': 'Hari Libur'})))

st.write('Hari kerja dan hari libur mempengaruhi penyewaan sepeda pada jam tertentu, di mana pada hari kerja penyewaan sepeda lebih tinggi pada jam 7-9 dan 16-19, sedangkan pada hari libur penyewaan sepeda lebih tinggi pada jam 10-16.')

# Visualisasi Bar Chart: Rata-rata Jumlah Peminjaman Sepeda per Hari dalam Seminggu
st.subheader('Rata-rata Jumlah Peminjaman Sepeda per Hari dalam Seminggu')
st.bar_chart(avg_rentals_per_day)

st.write('Berdasarkan hasil analisis data, ditemukan fakta bahwa peminjaman sepeda paling sering dilakukan pada hari Jumat. Lalu, ditemukan juga bahwa hari Minggu merupakan hari dengan peminjaman sepeda paling sedikit. Namun, perbedaan jumlah peminjaman sepeda pada hari Minggu dan hari lainnya tidak terlalu jauh. Oleh karena itu, dapat disimpulkan bahwa hari peminjaman tidak terlalu memengaruhi jumlah peminjaman sepeda.')