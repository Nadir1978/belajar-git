# Definisikan kelas 'Buku'
class Buku:
    # Constructor (__init__) untuk inisialisasi objek baru
    def __init__(self, judul, penulis, tahun):
        self.judul = judul  # Atribut judul buku
        self.penulis = penulis # Atribut penulis buku
        self.tahun = tahun # Atribut tahun terbit buku

    # Metode untuk menampilkan informasi buku
    def tampilkan_info(self):
        print("\n--- Info Buku ---")
        print(f"Judul: {self.judul}")
        print(f"Penulis: {self.penulis}")
        print(f"Tahun Terbit: {self.tahun}")

# --- Program Utama ---

# Meminta input dari pengguna
nama_buku = input("Masukkan judul buku: ")
nama_penulis = input("Masukkan nama penulis: ")
tahun_terbit = int(input("Masukkan tahun terbit (contoh: 2024): ")) # Mengonversi ke integer

# Membuat objek (instance) dari kelas 'Buku'
buku_saya = Buku(nama_buku, nama_penulis, tahun_terbit)

# Memanggil metode untuk menampilkan info buku yang sudah dibuat
buku_saya.tampilkan_info()

