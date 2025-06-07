💼 Aplikasi Koperasi Seragam Sekolah – Sistem Antrian & Pelayanan
Aplikasi berbasis Python untuk membantu pengelolaan antrian dan pencatatan pengambilan seragam siswa di sekolah. Dikembangkan khusus untuk kebutuhan internal koperasi sekolah.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📌 Fitur Utama
✅ Sistem login admin sederhana
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

🛠️ Cara Instalasi
📦 Menggunakan File .exe
Kompilasi file main.py menjadi .exe menggunakan perintah:

bash
Copy
Edit
pyinstaller --onefile main.py
Simpan main.exe dan koperasi_data.json dalam folder yang sama

Jalankan main.exe dengan klik dua kali

Tambahkan pengecualian jika dicegat Windows Defender

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🧑‍💻 Menjalankan Dari Kode Sumber
Clone repositori:

bash
Copy
Edit
git clone https://github.com/NamaAnda/RepoKoperasiSeragam
Masuk ke folder proyek:

bash
Copy
Edit
cd RepoKoperasiSeragam
Jalankan program:

bash
Copy
Edit
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
bash
Copy
Edit
.
├── main.py              # File utama aplikasi Python
├── koperasi_data.json   # File penyimpanan data (dibuat otomatis)
├── main.exe             # File executable (jika dikompilasi)
├── README.md            # Dokumentasi aplikasi
📄 Contoh Data (koperasi_data.json)
json
Copy
Edit
{
    "nomor_antrian_berikutnya": 3,
    "antrian": [
        { "nama": "Ani", "nomor_antrian": 1 },
        { "nama": "Budi", "nomor_antrian": 2 }
    ],
    "seragam_terambil": [
        { "nama": "Cici", "nomor_antrian": 0, "waktu_pengambilan": "2025-06-07 08:23:10" }
    ]
}

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📝 Lisensi
Aplikasi ini dibuat untuk keperluan edukasi dan dapat digunakan bebas untuk pengelolaan internal koperasi sekolah.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🙌 Kontributor
Nama: [Masukkan Nama Anda]

Sekolah: SMK / Sekolah Anda

Mata Pelajaran: Dasar Pemrograman Komputer (DPK)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

