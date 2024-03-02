# Proyek Analisis Data: Bike-sharing-dataset
- **Nama:** Raka Admiharfan Fatihah
- **Email:** m002d4ky2495@bangkit.academy
- **ID Dicoding:** raka_af

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

## - Visualisasi Data
