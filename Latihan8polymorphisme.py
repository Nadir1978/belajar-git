# ============================================
# PROGRAM 2: SISTEM PEMBAYARAN
# Konsep: Polymorphism dengan method overloading
# ============================================

class Pembayaran:
    def __init__(self, jumlah):
        self.jumlah = jumlah
    
    def proses_pembayaran(self):
        raise NotImplementedError("Metode harus diimplementasikan di subclass")
    
    def info(self):
        return f"Pembayaran sebesar Rp {self.jumlah:,}"

class Tunai(Pembayaran):
    def __init__(self, jumlah, uang_dibayar):
        super().__init__(jumlah)
        self.uang_dibayar = uang_dibayar
    
    def proses_pembayaran(self):
        kembalian = self.uang_dibayar - self.jumlah
        if kembalian >= 0:
            return f"✅ Pembayaran tunai berhasil!\n   Kembalian: Rp {kembalian:,}"
        else:
            return f"❌ Uang tidak cukup! Kurang: Rp {abs(kembalian):,}"
    
    def info(self):
        return f"{super().info()} - Metode: Tunai (Dibayar: Rp {self.uang_dibayar:,})"

class KartuKredit(Pembayaran):
    def __init__(self, jumlah, nama_kartu, nomor_kartu):
        super().__init__(jumlah)
        self.nama_kartu = nama_kartu
        self.nomor_kartu = nomor_kartu[-4:]  # Simpan hanya 4 digit terakhir
    
    def proses_pembayaran(self):
        # Simulasi validasi kartu kredit
        if len(self.nomor_kartu) == 4 and self.jumlah <= 10000000:
            return f"✅ Pembayaran dengan {self.nama_kartu} berhasil!\n   Kartu: ****-****-****-{self.nomor_kartu}"
        else:
            return "❌ Pembayaran kartu kredit gagal!"
    
    def info(self):
        return f"{super().info()} - Metode: Kartu Kredit ({self.nama_kartu})"

class EWallet(Pembayaran):
    def __init__(self, jumlah, provider, nomor_hp):
        super().__init__(jumlah)
        self.provider = provider
        self.nomor_hp = nomor_hp
    
    def proses_pembayaran(self):
        # Simulasi pembayaran e-wallet
        if self.jumlah <= 5000000:
            return f"✅ Pembayaran dengan {self.provider} berhasil!\n   No. HP: {self.nomor_hp}"
        else:
            return f"❌ Limit {self.provider} terlampaui! Maksimal Rp 5,000,000"
    
    def info(self):
        return f"{super().info()} - Metode: {self.provider}"

# ============================================
# PROGRAM UTAMA
# ============================================

def sistem_pembayaran():
    transaksi = []
    
    print("=" * 50)
    print("SISTEM PEMBAYARAN TOKO SERBA ADA")
    print("=" * 50)
    
    while True:
        print("\nMENU UTAMA:")
        print("1. Buat Transaksi Baru")
        print("2. Proses Semua Pembayaran")
        print("3. Lihat Riwayat Transaksi")
        print("4. Keluar")
        
        pilihan = input("\nPilih menu (1-4): ")
        
        if pilihan == "1":
            print("\n" + "-" * 30)
            print("TRANSAKSI BARU")
            print("-" * 30)
            
            jumlah = float(input("Masukkan jumlah pembayaran: Rp "))
            
            print("\nPilih metode pembayaran:")
            print("1. Tunai")
            print("2. Kartu Kredit")
            print("3. E-Wallet (GoPay/OVO/Dana)")
            
            metode = input("Pilih metode (1-3): ")
            
            if metode == "1":
                uang_dibayar = float(input("Uang yang dibayarkan: Rp "))
                pembayaran = Tunai(jumlah, uang_dibayar)
            
            elif metode == "2":
                nama_kartu = input("Jenis kartu (Visa/Mastercard): ")
                nomor_kartu = input("Nomor kartu (16 digit): ")
                pembayaran = KartuKredit(jumlah, nama_kartu, nomor_kartu)
            
            elif metode == "3":
                print("Pilih provider:")
                print("1. GoPay")
                print("2. OVO")
                print("3. Dana")
                provider_pilihan = input("Pilih (1-3): ")
                
                providers = {1: "GoPay", 2: "OVO", 3: "Dana"}
                provider = providers.get(int(provider_pilihan), "E-Wallet")
                
                nomor_hp = input("Nomor HP terdaftar: ")
                pembayaran = EWallet(jumlah, provider, nomor_hp)
            
            else:
                print("⚠ Metode tidak valid!")
                continue
            
            transaksi.append(pembayaran)
            print(f"\n✓ Transaksi berhasil ditambahkan!")
        
        elif pilihan == "2":
            if not transaksi:
                print("\n⚠ Tidak ada transaksi yang menunggu!")
            else:
                print("\n" + "=" * 50)
                print("MEMPROSES PEMBAYARAN")
                print("=" * 50)
                
                # POLYMORPHISM DI SINI!
                # Setiap objek punya metode proses_pembayaran() yang berbeda
                for i, pembayaran in enumerate(transaksi, 1):
                    print(f"\n[{i}] {pembayaran.info()}")
                    hasil = pembayaran.proses_pembayaran()
                    print(hasil)
        
        elif pilihan == "3":
            if not transaksi:
                print("\n⚠ Belum ada transaksi!")
            else:
                print("\n" + "=" * 50)
                print("RIWAYAT TRANSAKSI")
                print("=" * 50)
                
                for i, pembayaran in enumerate(transaksi, 1):
                    print(f"\n[{i}] {pembayaran.info()}")
        
        elif pilihan == "4":
            total_transaksi = sum(p.jumlah for p in transaksi)
            print(f"\nTotal transaksi hari ini: {len(transaksi)}")
            print(f"Total uang: Rp {total_transaksi:,.2f}")
            print("\nTerima kasih!")
            break
        
        else:
            print("⚠ Pilihan tidak valid!")

if __name__ == "__main__":
    sistem_pembayaran()