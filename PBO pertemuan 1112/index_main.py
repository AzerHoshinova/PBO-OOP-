class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.nilai = {}

    def tambah_nilai(self, mata_kuliah, nilai):
        self.nilai[mata_kuliah] = nilai
        print(f"Nilai {mata_kuliah} untuk {self.nama} ({self.nim}) ditambahkan: {nilai}")

    def lihat_nilai(self):
        print(f"Nilai-nilai {self.nama} ({self.nim}):")
        for mata_kuliah, nilai in self.nilai.items():
            print(f"{mata_kuliah}: {nilai}")

class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip = nip

    def beri_nilai(self, mahasiswa, mata_kuliah, nilai):
        mahasiswa.tambah_nilai(mata_kuliah, nilai)
        print(f"Dosen {self.nama} ({self.nip}) memberikan nilai {nilai} untuk {mata_kuliah} kepada {mahasiswa.nama} ({mahasiswa.nim})")
        
    
# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa("Reza", "2215061087")
mahasiswa2 = Mahasiswa("Laura", "2215061071")
mahasiswa3 = Mahasiswa("Dian", "2215061115")

# Membuat objek Dosen
dosen1 = Dosen("Pak Puput", "123456789")

# Interaksi: Dosen memberikan nilai kepada Mahasiswa
dosen1.beri_nilai(mahasiswa1, "Pemrograman Berorientasi Objek", 90)
dosen1.beri_nilai(mahasiswa2, "Pemrogaraman Berorientasi Objek", 90)
dosen1.beri_nilai(mahasiswa3, "Pemrogaraman Berorientasi Objek", 90)

# Mahasiswa melihat nilai mereka
mahasiswa1.lihat_nilai()
mahasiswa2.lihat_nilai()
mahasiswa3.lihat_nilai()
