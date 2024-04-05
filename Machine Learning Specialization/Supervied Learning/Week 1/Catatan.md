Regresi linear
Tentu! Berikut adalah ringkasan dari konten pada halaman ini:
- Video ini membahas tentang proses umum dari pembelajaran terawasi (supervised learning) dan model regresi linier.
- Model regresi linier adalah algoritma pembelajaran yang paling banyak digunakan di dunia saat ini.
- Contoh yang digunakan dalam video ini adalah memprediksi harga rumah berdasarkan ukuran rumah.
- Model regresi linier adalah contoh dari model pembelajaran terawasi yang disebut model regresi, karena memprediksi angka seperti harga dalam dolar.
- Ada juga model pembelajaran terawasi lainnya yang disebut model klasifikasi, yang memprediksi kategori atau kelas diskrit.
- Perbedaan antara klasifikasi dan regresi adalah bahwa klasifikasi memiliki jumlah output yang terbatas, sedangkan regresi memiliki jumlah output yang tak terbatas.
- Data dapat direpresentasikan dalam bentuk grafik atau tabel, dengan input (x) dan output (y) yang ingin diprediksi.
- Dataset yang digunakan untuk melatih model disebut set pelatihan (training set).
- Notasi standar dalam pembelajaran mesin digunakan untuk menggambarkan input (x), output (y), dan set pelatihan (training set).
- Fungsi (f) / model ini digunakan untuk memprediksi nilai yang diestimasikan (y-hat) berdasarkan input baru (x).
- Dalam pembelajaran terawasi, kita mencari cara untuk merepresentasikan fungsi f.
- Dalam contoh ini, kita menggunakan fungsi linear (garis lurus) sebagai dasar, yaitu f(x) = wx + b.
- Fungsi ini disebut regresi linear, khususnya regresi linear univariat karena hanya menggunakan satu variabel input.
- Ada juga regresi linear multivariat yang menggunakan beberapa variabel input.
- Selanjutnya, kita perlu membuat fungsi biaya (cost function) untuk melatih model dan menemukan nilai terbaik untuk w dan b.

Cost function:
- Video ini membahas tentang implementasi regresi linear dalam machine learning.
- Model regresi linear menggunakan parameter w dan b untuk memprediksi nilai output berdasarkan input.
- Nilai w dan b mempengaruhi bentuk garis regresi pada grafik.
- Tujuan regresi linear adalah memilih nilai w dan b sehingga garis regresi sesuai dengan data pelatihan.
- Untuk mengukur sejauh mana garis regresi cocok dengan data, digunakan fungsi biaya (cost function).
- Fungsi biaya dalam regresi linear umumnya menggunakan squared error cost function.
- Fungsi biaya ini menghitung selisih antara prediksi (y hat) dan target (y), kemudian mengkuadratkannya.
- Fungsi biaya ini kemudian dijumlahkan untuk semua contoh pelatihan dan dibagi dengan jumlah contoh pelatihan.
- Tujuan akhirnya adalah menemukan nilai w dan b yang membuat fungsi biaya seminimal mungkin.

![alt text](image.png)