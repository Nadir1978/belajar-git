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