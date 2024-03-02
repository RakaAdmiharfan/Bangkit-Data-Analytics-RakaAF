# Proyek Analisis Data: Bike-sharing-dataset
- **Nama:** Raka Admiharfan Fatihah
- **Email:** m002d4ky2495@bangkit.academy
- **ID Dicoding:** raka_af

# Setup Environment
1. pip install pipenv
2. pipenv install
3. pipenv shell
4. pip install numpy pandas scipy matplotlib seaborn jupyter

# Menjalankan Dashboard
1. cd .\dashboard\
2. streamlit run dashboard.py

# Deskripsi Proyek
Proyek ini adalah proyek analisis data dari dataset bike-sharing. Dataset ini berisi data dari tahun 2011 hingga 2012. Dataset ini memiliki 17 kolom dan 17389 baris pada data hour.csv dan 731 baris pada data day.csv. Kolom-kolom tersebut adalah:

1. `instant`: ID
2. `dteday`: Tanggal
3. `season`: Musim (1: musim dingin, 2: musim semi, 3: musim panas, 4: musim gugur)
4. `yr`: Tahun (0: 2011, 1: 2012)
5. `mnth`: Bulan (1 hingga 12)
6. `hr`: Jam (0 hingga 23)
7. `holiday`: Hari libur (0: bukan hari libur, 1: hari libur)
8. `weekday`: Hari dalam seminggu (0 hingga 6)
9. `workingday`: Hari kerja (0: bukan hari kerja, 1: hari kerja)
10. `weathersit`: Kondisi cuaca (1: cerah, 2: berkabut, 3: hujan ringan, 4: hujan lebat)
11. `temp`: Suhu dalam derajat Celsius
12. `atemp`: Suhu perasaan dalam derajat Celsius
13. `hum`: Kelembaban
14. `windspeed`: Kecepatan angin
15. `casual`: Jumlah peminjam sepeda yang tidak terdaftar
16. `registered`: Jumlah peminjam sepeda yang terdaftar
17. `cnt`: Jumlah total peminjam sepeda

# Proses Analisis Data
Proses analisis data ini terdiri dari beberapa tahap, yaitu:

## - Data Wrangling
1. **Data Gathering**: Load dan pengumpulan dataset yang digunakan. Dataset yang digunakan adalah `hour.csv` dan `day.csv`
2. **Data Assesing**: Melakukan pengecekan data untuk mengetahui apakah ada data yang tidak sesuai, seperti data yang hilang, duplikat, atau data yang tidak sesuai, dan mengecek tipe data dari setiap kolom. Pada tahap ini, ditemukan bahwa data tidak memiliki data yang hilang, duplikat, atau data yang tidak sesuai. Namun, terdapat kolom yang memiliki tipe data yang tidak sesuai.
3. **Data Cleaning**: Membersihkan data dari data yang tidak diperlukan. Pada tahap ini, dilakukan perubahan tipe data pada kolom `dteday` dan `season` pada data `hour.csv` dan `day.csv` yang sebelumnya bertipe `object` menjadi bertipe `datetime` dan `category` secara berurutan.

## - Exploratory Data Analysis (EDA)
Pada tahap ini, dilakukan analisis data untuk mengetahui hubungan antar variabel dan menemukan pola-pola yang terdapat pada data. Analisis yang dilakukan antara lain:

1. **Univariate Analysis**: Analisis yang dilakukan pada satu variabel, seperti distribusi data, frekuensi, dan lain-lain.
2. **Bivariate Analysis**: Analisis yang dilakukan pada dua variabel, seperti hubungan antar variabel, korelasi, dan lain-lain.
3. **Multivariate Analysis**: Analisis yang dilakukan pada lebih dari dua variabel, seperti hubungan antar variabel, korelasi, dan lain-lain.

Dari hasil analisis pada data hour.csv didapat hasil analisis, yaitu terdapat pola perilaku peminjaman sepeda berdasarkan jam (hr). Kita mendapatkan nilai rata-rata jam peminjaman adalah 11.54 dan standar deviasi 6.91. Dengan nilai tersebut maka variasi waktu peminjaman sepeda tidak terlalu tinggi dimana waktu peminjaman sepeda akan tidak terlalu jauh dengan nilai rata-rata.

Pada data day.csv didapat hasil analisis, yaitu didapat informasi rata-rata peminjaman sepeda berdasarkan workingday adalah 0.68 yang berarti rata-rata peminjaman sepeda pada hari kerja lebih tinggi dibandingkan hari libur. Lalu berdasarkan data rata-rata weekday peminjaman sepeda adalah 2.99 yang berarti rata-rata peminjaman sepeda lebih sering dilkakukan pada hari ke-3 pada setiap minggunya.

Berdasarkan eksplorasi data saya menghasilkan dua pertanyaan, yaitu:

- Pertanyaan 1 : Apakah terdapat pola perilaku peminjaman sepeda berdasarkan hari libur atau hari kerja dan apakah jam tertentu mempengaruhi penyewaan sepeda?
- Pertanyaan 2 : Apakah terdapat pola perilaku peminjaman sepeda berdasarkan hari pada setiap minggunya?

## - Visualisasi Data
Pada tahap ini, dilakukan visualisasi data untuk memperjelas hasil analisis yang telah dilakukan. Visualisasi yang dilakukan antara lain:

1. Bar Chart untuk menampilkan perbandingan antar variabel, contohnya yaitu rata-rata penyewaan sepeda pada hari kerja dan hari libur dan rata-rata penyewaan sepeda pada setiap hari dalam seminggu.
2. Line Chart untuk menampilkan perubahan data pada waktu tertentu, contohnya yaitu perubahan penyewaan sepeda pada jam tertentu.

# Kesimpulan
Dari hasil analisis data yang telah dilakukan, didapat beberapa kesimpulan, yaitu:

- Conclution pertanyaan 1 : Berdasarkan hasil analisis data, didapatkan fakta bahwa hari kerja atau libur tidak terlalu memengaruhi rata-rata jumlah penyewaan sepeda, dimana perbedaan nilai pada hari kerja dan libur hanya sebesar 254 sepeda. Kemudian hari kerja dan hari libur mempengaruhi penyewaan sepeda pada jam tertentu, dimana pada hari kerja penyewaan sepeda lebih tinggi pada jam 7-9 dan 16-19, sedangkan pada hari libur penyewaan sepeda lebih tinggi pada jam 10-16.

- Conclution pertanyaan 2 : Berdasarkan hasil analisis data, didapat fakta bahwa peminjaman sepeda paling sering dilakukan pada hari jumat. Lalu didapat fakta juga bahwa hari minggu merupakan hari dengan peminjaman sepeda paling sedikit. Namun perbedaan jumlah peminjaman sepeda pada hari minggu dan hari lainnya tidak terlalu jauh. Oleh karena itu didapatkan konklusi bahwa hari peminjaman tidak terlalu memengaruhi jumlah peminjaman sepeda.

# Dashboard
Terakhir pembuatan dashboard yang berisi visualisasi data yang telah dilakukan. Dashboard ini dibuat menggunakan module streamlit. Kode bisa dilihat pada folder dashboard/dashboard.py
