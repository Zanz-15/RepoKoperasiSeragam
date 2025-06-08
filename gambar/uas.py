import os
import json
import time

# --- Konfigurasi Login & File ---
USERNAME = "admin"       # Ganti sesuai kebutuhan
PASSWORD = "1234"        # Ganti sesuai kebutuhan
DATA_FILE = 'koperasi_data.json' # File untuk menyimpan data aplikasi

# --- Fungsi Login ---
def login():
    """Fungsi login sederhana sebelum mengakses menu utama."""
    clear_screen()
    print("===== LOGIN ADMIN KOPERASI =====")
    for _ in range(3):  # Maksimal 3 kali percobaan
        username_input = input("Username: ").strip()
        password_input = input("Password: ").strip()

        if username_input == USERNAME and password_input == PASSWORD:
            print("Login berhasil! Selamat datang.")
            time.sleep(1)
            return True
        else:
            print("Username atau password salah. Coba lagi.\n")
    print("Terlalu banyak percobaan gagal. Aplikasi keluar.")
    return False

# --- Fungsi Manajemen Data ---
def load_data():
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as file:
                data = json.load(file)
                if "nomor_antrian_berikutnya" not in data:
                    data["nomor_antrian_berikutnya"] = 1
                if "antrian" not in data:
                    data["antrian"] = []
                if "seragam_terambil" not in data:
                    data["seragam_terambil"] = []
                return data
    except (json.JSONDecodeError, FileNotFoundError):
        print("File data koperasi tidak ditemukan atau tidak valid. Memulai data baru.")
    return {
        "nomor_antrian_berikutnya": 1,
        "antrian": [],
        "seragam_terambil": []
    }

def save_data(data):
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Gagal menyimpan data koperasi: {e}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- Fungsi Logika Aplikasi ---
def register_for_uniform():
    clear_screen()
    print("===== Pendaftaran Pengambilan Seragam =====")
    student_name = input("Masukkan nama lengkap Anda: ").strip()

    if not student_name:
        print("Nama tidak boleh kosong. Silakan coba lagi.")
        input("Tekan Enter untuk melanjutkan...")
        return

    data = load_data()
    for entry in data["antrian"]:
        if entry["nama"].lower() == student_name.lower():
            print(f"\nAnda sudah terdaftar di antrian dengan nomor: {entry['nomor_antrian']}.")
            print("Mohon tunggu giliran Anda.")
            input("Tekan Enter untuk melanjutkan...")
            return
    for entry in data["seragam_terambil"]:
        if entry["nama"].lower() == student_name.lower():
            print(f"\nAnda sudah mengambil seragam. (Diambil pada: {entry['waktu_pengambilan']}).")
            input("Tekan Enter untuk melanjutkan...")
            return

    queue_number = data["nomor_antrian_berikutnya"]
    data["antrian"].append({"nama": student_name, "nomor_antrian": queue_number})
    data["nomor_antrian_berikutnya"] += 1
    save_data(data)

    print(f"\nSelamat, {student_name}! Anda mendapatkan nomor antrian: {queue_number}")
    print("Mohon tunggu giliran Anda.")
    input("Tekan Enter untuk kembali ke menu utama...")

def serve_student():
    clear_screen()
    print("===== Pelayanan Pengambilan Seragam =====")
    data = load_data()

    if not data["antrian"]:
        print("Tidak ada siswa dalam antrian saat ini.")
        input("Tekan Enter untuk melanjutkan...")
        return

    print("\n--- Antrian Saat Ini ---")
    for i, entry in enumerate(data["antrian"]):
        print(f"{i+1}. Nama: {entry['nama']}, Nomor Antrian: {entry['nomor_antrian']}")
    print("------------------------")

    expected_student = data["antrian"][0]
    print(f"\nNomor antrian yang sedang dilayani adalah: {expected_student['nomor_antrian']} ({expected_student['nama']})")

    try:
        current_queue_input = int(input("Masukkan nomor antrian siswa yang datang untuk dilayani: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor antrian.")
        input("Tekan Enter untuk melanjutkan...")
        return

    if current_queue_input == expected_student['nomor_antrian']:
        print(f"\nSiswa dengan nomor antrian {current_queue_input} ({expected_student['nama']}) siap dilayani.")
        confirm = input("Apakah seragam sudah diserahkan kepada siswa ini? (ya/tidak): ").lower()
        if confirm == 'ya':
            collected_entry = data["antrian"].pop(0)
            collected_entry["waktu_pengambilan"] = time.strftime("%Y-%m-%d %H:%M:%S")
            data["seragam_terambil"].append(collected_entry)
            save_data(data)
            print("Seragam berhasil diserahkan. Antrian bergeser.")
        else:
            print("Penyerahan seragam dibatalkan.")
    else:
        print(f"\nPERHATIAN: Nomor antrian yang Anda masukkan ({current_queue_input}) TIDAK SESUAI dengan nomor antrian yang sedang dilayani ({expected_student['nomor_antrian']}).")
        print("Siswa yang tidak sesuai antrian tidak akan dilayani. Mohon ikuti urutan antrian.")
    
    input("Tekan Enter untuk kembali ke menu utama...")

def view_queue_status():
    clear_screen()
    print("===== Status Antrian & Pengambilan Seragam =====")
    data = load_data()

    print("\n--- Antrian Saat Ini ---")
    if not data["antrian"]:
        print("Tidak ada siswa dalam antrian.")
    else:
        for i, entry in enumerate(data["antrian"]):
            print(f"{i+1}. Nama: {entry['nama']}, Nomor Antrian: {entry['nomor_antrian']}")
    
    print("\n--- Seragam Sudah Diambil ---")
    if not data["seragam_terambil"]:
        print("Belum ada seragam yang diambil.")
    else:
        for entry in data["seragam_terambil"]:
            print(f"Nama: {entry['nama']}, Nomor Antrian: {entry['nomor_antrian']}, Diambil: {entry['waktu_pengambilan']}")
    
    input("\nTekan Enter untuk kembali ke menu utama...")

def reset_data():
    clear_screen()
    print("===== RESET DATA KOPERASI =====")
    confirm = input("Anda yakin ingin mereset semua data antrian dan pengambilan seragam? (ya/tidak): ").lower()
    if confirm == 'ya':
        initial_data = {
            "nomor_antrian_berikutnya": 1,
            "antrian": [],
            "seragam_terambil": []
        }
        save_data(initial_data)
        print("Semua data koperasi telah direset.")
    else:
        print("Reset data dibatalkan.")
    input("Tekan Enter untuk kembali ke menu utama...")

# --- Menu Utama ---
def main_menu():
    while True:
        clear_screen()
        print("===== Aplikasi Koperasi Seragam Sekolah =====")
        print("1. Daftar & Ambil Nomor Antrian")
        print("2. Layani Siswa (Untuk Petugas Koperasi)")
        print("3. Lihat Status Antrian & Pengambilan")
        print("4. Reset Data Koperasi (Hanya Untuk Admin)")
        print("5. Keluar")
        
        choice = input("Pilih opsi (1-5): ").strip()

        if choice == '1':
            register_for_uniform()
        elif choice == '2':
            serve_student()
        elif choice == '3':
            view_queue_status()
        elif choice == '4':
            reset_data()
        elif choice == '5':
            print("Terima kasih telah menggunakan aplikasi koperasi. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 dan 5.")
            input("Tekan Enter untuk mencoba lagi...")

# --- Jalankan aplikasi ---
if __name__ == "__main__":
    if login():
        main_menu()
