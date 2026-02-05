# Kelas Induk (Parent Class)
class Minuman:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def tampilkan_info_minuman(self):
        print(f"Nama Minuman: {self.nama}")
        print(f"Harga: Rp {self.harga}")

# Kelas Anak (Child Class) yang mewarisi dari Minuman
class JenisMinuman(Minuman):
    def __init__(self, nama, harga, jenis_spesifik):
        # Memanggil __init__ dari kelas induk (Minuman)
        super().__init__(nama, harga)
        self.jenis_spesifik = jenis_spesifik # Atribut baru untuk kelas anak

    # Method baru atau override method dari kelas induk (opsional)
    def tampilkan_info_lengkap(self):
        self.tampilkan_info_minuman() # Menggunakan method dari kelas induk
        print(f"Jenis Spesifik: {self.jenis_spesifik}")
        print("-" * 20)

# --- Program Utama ---
if __name__ == "__main__":
    print("--- Program Input Data Minuman (OOP Inheritance) ---")

    # Input dari pengguna
    nama_input = input("Masukkan nama minuman: ")
    harga_input_str = input("Masukkan harga minuman (angka): ")
    jenis_spesifik_input = input("Masukkan jenis spesifik (misal: Dingin/Panas/Manis): ")

    # Konversi input harga ke integer/float
    try:
        harga_input = int(harga_input_str)
    except ValueError:
        print("Harga tidak valid. Menggunakan 0.")
        harga_input = 0

    # Membuat objek dari kelas anak
    minuman_saya = JenisMinuman(nama_input, harga_input, jenis_spesifik_input)

    # Menampilkan informasi menggunakan method kelas anak (yang memanggil method induk)
    print("\n--- Detail Minuman ---")
    minuman_saya.tampilkan_info_lengkap()

