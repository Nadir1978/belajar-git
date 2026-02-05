# 1. Mendefinisikan Kelas (Class) 'Mobil'
class Mobil:
    # __init__ adalah method konstruktor untuk inisialisasi atribut saat objek dibuat
    def __init__(self, merk, warna):
        self.merk = merk    # Atribut (data)
        self.warna = warna  # Atribut (data)

    # Method (fungsi) untuk perilaku objek
    def maju(self):
        return f"Mobil {self.merk} berwarna {self.warna} sedang berjalan..."

    def gantiWarna(self, warna_baru):
        self.warna = warna_baru
        return f"Warna mobil {self.merk} telah diubah menjadi {self.warna}"

# 2. Membuat Objek (Instance) dari Kelas 'Mobil'
mobil_saya = Mobil("Toyota", "Merah")
mobil_teman = Mobil("Honda", "Biru")

# 3. Mengakses Atribut dan Memanggil Method
print(mobil_saya.merk)       # Output: Toyota
print(mobil_teman.warna)     # Output: Biru
print(mobil_saya.maju())     # Output: Mobil Toyota berwarna Merah sedang berjalan...

# 4. Mengubah Atribut melalui Method
print(mobil_teman.gantiWarna("Kuning")) # Output: Warna mobil Honda telah diubah menjadi Kuning
print(mobil_teman.maju())              # Output: Mobil Honda berwarna Kuning sedang berjalan...

# Contoh dengan Pewarisan (Inheritance)
class MobilSport(Mobil): # MobilSport mewarisi dari Mobil
    def __init__(self, merk, warna, turbo):
        super().__init__(merk, warna) # Memanggil konstruktor kelas induk
        self.turbo = turbo

    def boost(self):
        return f"Mobil {self.merk} {self.warna} menyala mode Turbo!"

mobil_sport_saya = MobilSport("Ferrari", "Merah", True)
print(mobil_sport_saya.maju()) # Bisa menggunakan method dari kelas induk
print(mobil_sport_saya.boost()) # Bisa menggunakan method khusus kelas anak
