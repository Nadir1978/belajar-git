# ============================================
# PROGRAM 1: BENTUK GEOMETRI
# Konsep: Polymorphism dengan method overriding
# ============================================

class Bentuk:
    def __init__(self, nama):
        self.nama = nama
    
    def hitung_luas(self):
        raise NotImplementedError("Subclass harus implementasi ini")
    
    def hitung_keliling(self):
        raise NotImplementedError("Subclass harus implementasi ini")
    
    def info(self):
        return f"Bentuk: {self.nama}"

class Persegi(Bentuk):
    def __init__(self, sisi):
        super().__init__("Persegi")
        self.sisi = sisi
    
    def hitung_luas(self):
        return self.sisi * self.sisi
    
    def hitung_keliling(self):
        return 4 * self.sisi
    
    def info(self):
        return f"{super().info()} dengan sisi {self.sisi} cm"

class PersegiPanjang(Bentuk):
    def __init__(self, panjang, lebar):
        super().__init__("Persegi Panjang")
        self.panjang = panjang
        self.lebar = lebar
    
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def info(self):
        return f"{super().info()} dengan panjang {self.panjang} cm dan lebar {self.lebar} cm"

class Lingkaran(Bentuk):
    def __init__(self, jari_jari):
        super().__init__("Lingkaran")
        self.jari_jari = jari_jari
    
    def hitung_luas(self):
        return 3.14 * self.jari_jari * self.jari_jari
    
    def hitung_keliling(self):
        return 2 * 3.14 * self.jari_jari
    
    def info(self):
        return f"{super().info()} dengan jari-jari {self.jari_jari} cm"

class Segitiga(Bentuk):
    def __init__(self, alas, tinggi):
        super().__init__("Segitiga")
        self.alas = alas
        self.tinggi = tinggi
    
    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi
    
    def hitung_keliling(self):
        # Diasumsikan segitiga sama sisi untuk sederhana
        return 3 * self.alas
    
    def info(self):
        return f"{super().info()} dengan alas {self.alas} cm dan tinggi {self.tinggi} cm"

# ============================================
# PROGRAM UTAMA DENGAN INPUT USER
# ============================================

def hitung_bentuk():
    daftar_bentuk = []
    
    print("=" * 50)
    print("PROGRAM PENGHITUNG LUAS DAN KELILING BENTUK")
    print("=" * 50)
    
    while True:
        print("\nPilih bentuk yang ingin dihitung:")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Lingkaran")
        print("4. Segitiga")
        print("5. Tampilkan semua hasil")
        print("6. Keluar")
        
        pilihan = input("\nMasukkan pilihan (1-6): ")
        
        if pilihan == "1":
            sisi = float(input("Masukkan panjang sisi (cm): "))
            bentuk = Persegi(sisi)
            daftar_bentuk.append(bentuk)
            print(f"✓ Persegi dengan sisi {sisi} cm berhasil dibuat")
        
        elif pilihan == "2":
            panjang = float(input("Masukkan panjang (cm): "))
            lebar = float(input("Masukkan lebar (cm): "))
            bentuk = PersegiPanjang(panjang, lebar)
            daftar_bentuk.append(bentuk)
            print(f"✓ Persegi panjang {panjang} x {lebar} cm berhasil dibuat")
        
        elif pilihan == "3":
            jari = float(input("Masukkan jari-jari (cm): "))
            bentuk = Lingkaran(jari)
            daftar_bentuk.append(bentuk)
            print(f"✓ Lingkaran dengan jari-jari {jari} cm berhasil dibuat")
        
        elif pilihan == "4":
            alas = float(input("Masukkan alas (cm): "))
            tinggi = float(input("Masukkan tinggi (cm): "))
            bentuk = Segitiga(alas, tinggi)
            daftar_bentuk.append(bentuk)
            print(f"✓ Segitiga dengan alas {alas} cm dan tinggi {tinggi} cm berhasil dibuat")
        
        elif pilihan == "5":
            if not daftar_bentuk:
                print("\n⚠ Belum ada bentuk yang dibuat!")
            else:
                print("\n" + "=" * 50)
                print("HASIL PERHITUNGAN")
                print("=" * 50)
                
                total_luas = 0
                total_keliling = 0
                
                # POLYMORPHISM DI SINI!
                # Meskipun tipe objek berbeda, kita bisa panggil method yang sama
                for bentuk in daftar_bentuk:
                    print(f"\n{bentuk.info()}")
                    luas = bentuk.hitung_luas()
                    keliling = bentuk.hitung_keliling()
                    print(f"  Luas: {luas:.2f} cm²")
                    print(f"  Keliling: {keliling:.2f} cm")
                    
                    total_luas += luas
                    total_keliling += keliling
                
                print(f"\n{'=' * 30}")
                print(f"TOTAL SEMUA BENTUK:")
                print(f"Jumlah bentuk: {len(daftar_bentuk)}")
                print(f"Total luas: {total_luas:.2f} cm²")
                print(f"Total keliling: {total_keliling:.2f} cm")
        
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan program!")
            break
        
        else:
            print("⚠ Pilihan tidak valid! Silakan pilih 1-6")

if __name__ == "__main__":
    hitung_bentuk()