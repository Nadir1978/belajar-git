# ============================================
# SISTEM INVENTARIS TOKO - INPUT INTERAKTIF
# ============================================

class Produk:
    def __init__(self, kode, nama, harga, stok):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.stok = stok
    
    def update_stok(self, jumlah):
        self.stok += jumlah
        return self.stok
    
    def display_info(self):
        return f"{self.kode} | {self.nama} | Rp {self.harga:,} | Stok: {self.stok}"

class Elektronik(Produk):
    def __init__(self, kode, nama, harga, stok, garansi, merk):
        super().__init__(kode, nama, harga, stok)
        self.garansi = garansi  # dalam bulan
        self.merk = merk
    
    def display_info(self):
        info_dasar = super().display_info()
        return f"{info_dasar} | Merk: {self.merk} | Garansi: {self.garansi} bulan"

class Aksesoris(Produk):
    def __init__(self, kode, nama, harga, stok, warna, material):
        super().__init__(kode, nama, harga, stok)
        self.warna = warna
        self.material = material
    
    def display_info(self):
        info_dasar = super().display_info()
        return f"{info_dasar} | Warna: {self.warna} | Material: {self.material}"

def input_produk():
    print("\n" + "="*50)
    print("INPUT PRODUK BARU")
    print("="*50)
    
    kode = input("Kode produk: ")
    nama = input("Nama produk: ")
    harga = float(input("Harga: "))
    stok = int(input("Stok awal: "))
    
    print("\nKategori produk:")
    print("1. Elektronik")
    print("2. Aksesoris")
    kategori = input("Pilih kategori (1/2): ")
    
    if kategori == "1":
        merk = input("Merk: ")
        garansi = int(input("Garansi (bulan): "))
        return Elektronik(kode, nama, harga, stok, garansi, merk)
    else:
        warna = input("Warna: ")
        material = input("Material: ")
        return Aksesoris(kode, nama, harga, stok, warna, material)

def sistem_inventaris():
    inventaris = []
    
    while True:
        print("\n" + "="*50)
        print("SISTEM INVENTARIS TOKO ELEKTRONIK")
        print("="*50)
        print("1. Tambah Produk Baru")
        print("2. Tampilkan Semua Produk")
        print("3. Update Stok Produk")
        print("4. Cari Produk")
        print("5. Jual Produk")
        print("6. Laporan")
        print("7. Keluar")
        
        pilihan = input("\nPilih menu (1-7): ")
        
        if pilihan == "1":
            produk = input_produk()
            inventaris.append(produk)
            print(f"\n✓ Produk '{produk.nama}' berhasil ditambahkan!")
        
        elif pilihan == "2":
            if not inventaris:
                print("\n⚠ Inventaris kosong!")
            else:
                print("\n" + "="*50)
                print("DAFTAR PRODUK")
                print("="*50)
                
                print("\n📱 ELEKTRONIK:")
                elektronik = [p for p in inventaris if isinstance(p, Elektronik)]
                if elektronik:
                    for p in elektronik:
                        print(f"  - {p.display_info()}")
                else:
                    print("  (Tidak ada produk)")
                
                print("\n💎 AKSESORIS:")
                aksesoris = [p for p in inventaris if isinstance(p, Aksesoris)]
                if aksesoris:
                    for p in aksesoris:
                        print(f"  - {p.display_info()}")
                else:
                    print("  (Tidak ada produk)")
        
        elif pilihan == "3":
            if not inventaris:
                print("\n⚠ Inventaris kosong!")
                continue
            
            print("\nDaftar Produk:")
            for i, p in enumerate(inventaris, 1):
                print(f"{i}. {p.nama} (Stok: {p.stok})")
            
            idx = int(input("\nPilih nomor produk: ")) - 1
            if 0 <= idx < len(inventaris):
                produk = inventaris[idx]
                print(f"\nProduk: {produk.nama}")
                print(f"Stok saat ini: {produk.stok}")
                
                aksi = input("\n1. Tambah stok\n2. Kurangi stok\nPilih (1/2): ")
                jumlah = int(input("Jumlah: "))
                
                if aksi == "1":
                    produk.update_stok(jumlah)
                    print(f"✓ Stok berhasil ditambah! Stok sekarang: {produk.stok}")
                elif aksi == "2":
                    if jumlah > produk.stok:
                        print("✗ Jumlah melebihi stok yang tersedia!")
                    else:
                        produk.update_stok(-jumlah)
                        print(f"✓ Stok berhasil dikurangi! Stok sekarang: {produk.stok}")
                else:
                    print("Pilihan tidak valid!")
            else:
                print("Pilihan tidak valid!")
        
        elif pilihan == "4":
            if not inventaris:
                print("\n⚠ Inventaris kosong!")
                continue
            
            keyword = input("Masukkan kode atau nama produk: ").lower()
            hasil = []
            
            for p in inventaris:
                if keyword in p.kode.lower() or keyword in p.nama.lower():
                    hasil.append(p)
            
            if hasil:
                print(f"\nDitemukan {len(hasil)} produk:")
                for p in hasil:
                    print(f"\n{p.display_info()}")
            else:
                print("\n✗ Produk tidak ditemukan!")
        
        elif pilihan == "5":
            if not inventaris:
                print("\n⚠ Inventaris kosong!")
                continue
            
            print("\nPROSES PENJUALAN")
            print("-" * 30)
            
            keranjang = []
            total_harga = 0
            
            while True:
                print("\nDaftar Produk Tersedia:")
                produk_tersedia = [p for p in inventaris if p.stok > 0]
                
                if not produk_tersedia:
                    print("Tidak ada produk yang tersedia!")
                    break
                
                for i, p in enumerate(produk_tersedia, 1):
                    print(f"{i}. {p.nama} - Rp {p.harga:,} (Stok: {p.stok})")
                
                pilihan_produk = input("\nPilih produk (atau 'selesai' untuk checkout): ")
                
                if pilihan_produk.lower() == 'selesai':
                    break
                
                try:
                    idx = int(pilihan_produk) - 1
                    if 0 <= idx < len(produk_tersedia):
                        produk = produk_tersedia[idx]
                        jumlah = int(input(f"Jumlah {produk.nama}: "))
                        
                        if jumlah > produk.stok:
                            print(f"✗ Stok tidak cukup! Stok tersedia: {produk.stok}")
                        else:
                            keranjang.append({
                                'produk': produk,
                                'jumlah': jumlah,
                                'subtotal': produk.harga * jumlah
                            })
                            total_harga += produk.harga * jumlah
                            print(f"✓ {produk.nama} x{jumlah} ditambahkan ke keranjang")
                    else:
                        print("Pilihan tidak valid!")
                except ValueError:
                    print("Input tidak valid!")
            
            if keranjang:
                print("\n" + "="*50)
                print("STRUK PENJUALAN")
                print("="*50)
                
                for item in keranjang:
                    produk = item['produk']
                    print(f"{produk.nama} x{item['jumlah']}: Rp {item['subtotal']:,}")
                    produk.update_stok(-item['jumlah'])
                
                print("-" * 30)
                print(f"TOTAL: Rp {total_harga:,}")
                
                bayar = float(input("\nJumlah uang pembayaran: Rp "))
                if bayar >= total_harga:
                    kembalian = bayar - total_harga
                    print(f"Kembalian: Rp {kembalian:,.2f}")
                    print("\n✅ Transaksi berhasil!")
                else:
                    print(f"\n❌ Uang tidak cukup! Kurang: Rp {total_harga - bayar:,.2f}")
        
        elif pilihan == "6":
            if not inventaris:
                print("\n⚠ Inventaris kosong!")
                continue
            
            total_produk = len(inventaris)
            total_nilai = sum(p.harga * p.stok for p in inventaris)
            produk_kosong = sum(1 for p in inventaris if p.stok == 0)
            
            print("\n" + "="*50)
            print("LAPORAN INVENTARIS")
            print("="*50)
            print(f"Total Produk: {total_produk}")
            print(f"Total Nilai Inventaris: Rp {total_nilai:,.2f}")
            print(f"Produk Habis: {produk_kosong}")
            print(f"Produk Tersedia: {total_produk - produk_kosong}")
            
            # Produk dengan stok terendah
            produk_stok_min = min(inventaris, key=lambda x: x.stok)
            print(f"\nProduk Stok Terendah: {produk_stok_min.nama} (Stok: {produk_stok_min.stok})")
            
            # Produk dengan stok tertinggi
            produk_stok_max = max(inventaris, key=lambda x: x.stok)
            print(f"Produk Stok Tertinggi: {produk_stok_max.nama} (Stok: {produk_stok_max.stok})")
        
        elif pilihan == "7":
            print("\nTerima kasih telah menggunakan sistem inventaris!")
            break
        
        else:
            print("\n⚠ Pilihan tidak valid! Silakan pilih 1-7")

if __name__ == "__main__":
    sistem_inventaris()