💼 Aplikasi Koperasi Seragam Sekolah – Sistem Antrian & Pelayanan
Aplikasi berbasis Python untuk membantu pengelolaan antrian dan pencatatan pengambilan seragam siswa di sekolah. Dikembangkan khusus untuk kebutuhan internal koperasi sekolah.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📌 Fitur Utama

✅ Sistem login admin sederhana

  Username = admin

  password = 1234

✅ Pendaftaran siswa untuk pengambilan seragam dengan nomor antrian otomatis

✅ Pelayanan siswa berdasarkan urutan antrian

✅ Pencatatan waktu pengambilan seragam

✅ Menyimpan dan memuat data dalam file koperasi_data.json

✅ Fitur reset seluruh data antrian dan pengambilan

✅ Validasi input nama dan nomor antrian

✅ Tampilan status antrian dan siswa yang sudah dilayani

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧰 Teknologi yang Digunakan
Bahasa Pemrograman: Python 3

Modul Bawaan: json, os, time

Tidak menggunakan library eksternal

Bisa dikompilasi menjadi .exe menggunakan PyInstaller

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

cara download file .exe 

1. klik pada bagian dist
2. klik pada file uas .exe
3. klik raw dipojok kanan atas

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


🛠️ Cara Instalasi
📦 Menggunakan File .exe
Kompilasi file main.py menjadi .exe menggunakan perintah:

pyinstaller --onefile main.py
Simpan main.exe dan koperasi_data.json dalam folder yang sama

Jalankan main.exe dengan klik dua kali

Tambahkan pengecualian jika dicegat Windows Defender

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧑‍💻 Menjalankan Dari Kode Sumber
Clone repositori:

git clone https://github.com/Zanz-15/RepoKoperasiSeragam
Masuk ke folder proyek:

cd RepoKoperasiSeragam
Jalankan program:

python main.py

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

👨‍🏫 Panduan Pengguna
Login dengan username dan password admin

Pilih menu:

1: Daftarkan siswa (input nama → dapat nomor antrian)

2: Layani siswa sesuai nomor antrian → konfirmasi penyerahan seragam

3: Tampilkan antrian aktif dan data siswa yang sudah dilayani

4: Reset semua data

5: Keluar dari aplikasi

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📁 Struktur Folder

├── main.py              # File utama aplikasi Python

├── koperasi_data.json   # File penyimpanan data (dibuat otomatis)

├── main.exe             # File executable (jika dikompilasi)

├── README.md            # Dokumentasi aplikasi


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📝 Lisensi
Aplikasi ini dibuat untuk keperluan edukasi dan dapat digunakan bebas untuk pengelolaan internal koperasi sekolah.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🙌 Kontributor
Nama:

      [Muhammad Zakiy Alfawaz/23]
      
      [Muhammad Diego Gustav Al-Ghazali/21]
      
      [Muhammad Dhanil Dwi Cahyono/20]
      
Sekolah: SMK Negeri 1 Probolinggo

Mata Pelajaran: Dasar Pemrograman Komputer (DPK)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

NOTE : jika ingin melihat fitur nya sudah ada di bagian folder gambar dan sudah lengkap dengan flowchart nya dan data untuk .exe ada di dalam folder dist


