# ============================================
# CONTOH 1: SISTEM AKADEMIK - INPUT INTERAKTIF
# ============================================

class Person:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
    
    def display_info(self):
        return f"Nama: {self.nama}, Umur: {self.umur} tahun"

class Mahasiswa(Person):
    def __init__(self, nama, umur, nim, jurusan):
        super().__init__(nama, umur)
        self.nim = nim
        self.jurusan = jurusan
        self.nilai_matkul = []
    
    def input_nilai(self):
        jumlah = int(input(f"Berapa mata kuliah untuk {self.nama}? "))
        for i in range(jumlah):
            matkul = input(f"Nama mata kuliah ke-{i+1}: ")
            nilai = float(input(f"Nilai {matkul}: "))
            self.nilai_matkul.append({"matkul": matkul, "nilai": nilai})
    
    def hitung_ipk(self):
        if not self.nilai_matkul:
            return 0.0
        total = sum(item['nilai'] for item in self.nilai_matkul)
        return total / len(self.nilai_matkul)
    
    def display_info(self):
        info_dasar = super().display_info()
        info_mahasiswa = f"{info_dasar}\nNIM: {self.nim}, Jurusan: {self.jurusan}"
        
        if self.nilai_matkul:
            info_mahasiswa += "\n\nDaftar Nilai:"
            for item in self.nilai_matkul:
                info_mahasiswa += f"\n  - {item['matkul']}: {item['nilai']}"
            info_mahasiswa += f"\n\nIPK: {self.hitung_ipk():.2f}"
        
        return info_mahasiswa

def input_mahasiswa():
    print("\n" + "="*50)
    print("INPUT DATA MAHASISWA")
    print("="*50)
    
    nama = input("Nama mahasiswa: ")
    umur = int(input("Umur: "))
    nim = input("NIM: ")
    jurusan = input("Jurusan: ")
    
    mhs = Mahasiswa(nama, umur, nim, jurusan)
    
    # Input nilai mata kuliah
    input_nilai = input("Apakah ingin input nilai mata kuliah? (y/n): ").lower()
    if input_nilai == 'y':
        mhs.input_nilai()
    
    return mhs

# ============================================
# CONTOH 2: SISTEM BUKU PERPUSTAKAAN - INPUT USER
# ============================================

class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = "Tersedia"  # Tersedia/Dipinjam
    
    def pinjam(self):
        if self.status == "Tersedia":
            self.status = "Dipinjam"
            return True
        return False
    
    def kembalikan(self):
        self.status = "Tersedia"
    
    def display_info(self):
        return f"{self.judul} - {self.penulis} ({self.tahun}) [{self.status}]"

class BukuFiksi(Buku):
    def __init__(self, judul, penulis, tahun, genre):
        super().__init__(judul, penulis, tahun)
        self.genre = genre
    
    def display_info(self):
        info_dasar = super().display_info()
        return f"{info_dasar} | Genre: {self.genre}"

class BukuNonFiksi(Buku):
    def __init__(self, judul, penulis, tahun, subjek):
        super().__init__(judul, penulis, tahun)
        self.subjek = subjek
    
    def display_info(self):
        info_dasar = super().display_info()
        return f"{info_dasar} | Subjek: {self.subjek}"

def input_buku():
    print("\n" + "="*50)
    print("INPUT DATA BUKU")
    print("="*50)
    
    judul = input("Judul buku: ")
    penulis = input("Penulis: ")
    tahun = input("Tahun terbit: ")
    
    print("\nTipe buku:")
    print("1. Buku Fiksi")
    print("2. Buku Non-Fiksi")
    tipe = input("Pilih tipe (1/2): ")
    
    if tipe == "1":
        genre = input("Genre (Novel/Komik/Cerpen/dll): ")
        buku = BukuFiksi(judul, penulis, tahun, genre)
    else:
        subjek = input("Subjek (Sains/Sejarah/Teknologi/dll): ")
        buku = BukuNonFiksi(judul, penulis, tahun, subjek)
    
    return buku

# ============================================
# PROGRAM UTAMA
# ============================================

def main():
    daftar_mahasiswa = []
    daftar_buku = []
    
    while True:
        print("\n" + "="*50)
        print("SISTEM AKADEMIK & PERPUSTAKAAN")
        print("="*50)
        print("1. Input Data Mahasiswa")
        print("2. Input Data Buku")
        print("3. Tampilkan Semua Mahasiswa")
        print("4. Tampilkan Semua Buku")
        print("5. Pinjam Buku")
        print("6. Keluar")
        
        pilihan = input("\nPilih menu (1-6): ")
        
        if pilihan == "1":
            mhs = input_mahasiswa()
            daftar_mahasiswa.append(mhs)
            print(f"\n✓ Data mahasiswa {mhs.nama} berhasil disimpan!")
        
        elif pilihan == "2":
            buku = input_buku()
            daftar_buku.append(buku)
            print(f"\n✓ Data buku '{buku.judul}' berhasil disimpan!")
        
        elif pilihan == "3":
            if not daftar_mahasiswa:
                print("\n⚠ Belum ada data mahasiswa!")
            else:
                print("\n" + "="*50)
                print("DAFTAR MAHASISWA")
                print("="*50)
                for i, mhs in enumerate(daftar_mahasiswa, 1):
                    print(f"\n[{i}] {mhs.display_info()}")
        
        elif pilihan == "4":
            if not daftar_buku:
                print("\n⚠ Belum ada data buku!")
            else:
                print("\n" + "="*50)
                print("DAFTAR BUKU")
                print("="*50)
                for i, buku in enumerate(daftar_buku, 1):
                    print(f"[{i}] {buku.display_info()}")
        
        elif pilihan == "5":
            if not daftar_mahasiswa or not daftar_buku:
                print("\n⚠ Data mahasiswa atau buku masih kosong!")
                continue
            
            # Tampilkan daftar mahasiswa
            print("\nDaftar Mahasiswa:")
            for i, mhs in enumerate(daftar_mahasiswa, 1):
                print(f"{i}. {mhs.nama} (NIM: {mhs.nim})")
            
            # Pilih mahasiswa
            idx_mhs = int(input("\nPilih nomor mahasiswa: ")) - 1
            if 0 <= idx_mhs < len(daftar_mahasiswa):
                mhs = daftar_mahasiswa[idx_mhs]
                
                # Tampilkan daftar buku
                print("\nDaftar Buku Tersedia:")
                buku_tersedia = [b for b in daftar_buku if b.status == "Tersedia"]
                
                if not buku_tersedia:
                    print("Tidak ada buku yang tersedia!")
                else:
                    for i, buku in enumerate(buku_tersedia, 1):
                        print(f"{i}. {buku.judul}")
                    
                    # Pilih buku
                    idx_buku = int(input("\nPilih nomor buku: ")) - 1
                    if 0 <= idx_buku < len(buku_tersedia):
                        buku = buku_tersedia[idx_buku]
                        if buku.pinjam():
                            print(f"\n✓ Buku '{buku.judul}' berhasil dipinjam oleh {mhs.nama}")
                        else:
                            print(f"\n✗ Buku '{buku.judul}' sedang tidak tersedia")
                    else:
                        print("Pilihan tidak valid!")
            else:
                print("Pilihan tidak valid!")
        
        elif pilihan == "6":
            print("\nTerima kasih telah menggunakan sistem ini!")
            break
        
        else:
            print("\n⚠ Pilihan tidak valid! Silakan pilih 1-6")

if __name__ == "__main__":
    main()