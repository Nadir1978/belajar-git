class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik        # Public
        self.__saldo = saldo          # Private (Disembunyikan)

    # Getter: Cara aman melihat saldo
    def cek_saldo(self):
        return f"Saldo milik {self.pemilik} adalah Rp{self.__saldo}"

    # Setter: Cara aman menambah saldo (dengan validasi)
    def setor_uang(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f"Berhasil setor Rp{jumlah}")
        else:
            print("Jumlah setoran harus positif!")

# --- Penggunaan ---
akun = RekeningBank("Budi", 1000000)

# 1. Mencoba akses langsung (Akan Error)
# print(akun.__saldo) 

# 2. Mengakses via Getter
print(akun.cek_saldo()) # Output: Saldo milik Budi adalah Rp1000000

# 3. Mengubah via Setter
akun.setor_uang(500000)
print(akun.cek_saldo()) # Output: Saldo milik Budi adalah Rp1500000
