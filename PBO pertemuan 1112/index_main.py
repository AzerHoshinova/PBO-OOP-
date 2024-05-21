class Mahasiswa:
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan
        self.krs = {}
        self.nilai = {}

    def tambah_matakuliah(self, matakuliah):
        self.krs[matakuliah] = None  # Nilai awal adalah None
        print(f"{self.nama} menambahkan mata kuliah {matakuliah} ke dalam KRS.")

    def tampilkan_krs(self):
        print(f"KRS {self.nama} ({self.npm} - {self.jurusan}):")
        for matakuliah in self.krs:
            print(f" - {matakuliah} (Nilai: {self.nilai.get(matakuliah, 'Belum Ada Nilai')})")

    def lihat_nilai(self):
        print(f"Nilai {self.nama} ({self.npm} - {self.jurusan}):")
        for matakuliah, nilai in self.nilai.items():
            print(f" - {matakuliah}: {nilai}")

    def tambah_nilai(self, matakuliah, nilai):
        if matakuliah in self.krs:
            self.nilai[matakuliah] = nilai
            print(f"Nilai {nilai} untuk mata kuliah {matakuliah} ditambahkan kepada {self.nama}.")
        else:
            print(f"{self.nama} tidak mengambil mata kuliah {matakuliah}, nilai tidak dapat ditambahkan.")

class Dosen:
    def __init__(self, nama, nidn, jurusan):
        self.nama = nama
        self.nidn = nidn
        self.jurusan = jurusan
        self.mengajar = []

    def tambah_matakuliah(self, matakuliah):
        self.mengajar.append(matakuliah)
        print(f"{self.nama} menambahkan mata kuliah {matakuliah} yang diajarkan.")

    def tampilkan_matakuliah(self):
        print(f"Daftar mata kuliah yang diajarkan oleh {self.nama} ({self.nidn} - {self.jurusan}):")
        for matakuliah in self.mengajar:
            print(f" - {matakuliah}")

    def tambah_nilai(self, mahasiswa, matakuliah, nilai):
        if matakuliah in self.mengajar:
            mahasiswa.tambah_nilai(matakuliah, nilai)
        else:
            print(f"Dosen {self.nama} tidak mengajar mata kuliah {matakuliah}, nilai tidak dapat ditambahkan.")

# Membuat objek dari kelas Mahasiswa
mahasiswa1 = Mahasiswa("Reza", "2215061087", "Teknik Informatika")
mahasiswa2 = Mahasiswa("Laura", "2215061071", "Teknik Informatika")
mahasiswa3 = Mahasiswa("Dian", "22150610115", "Teknik Informatika")

# Membuat objek dari kelas Dosen
dosen1 = Dosen("Pak Puput", "000112233", "Teknik Informatika")
dosen2 = Dosen("Bu Yessi", "000445566", "Teknik Informatika")
dosen3 = Dosen("Pak Mona", "000411565", "Teknik Informatika")

# Menambah mata kuliah yang diajarkan oleh dosen
dosen1.tambah_matakuliah("Pemrograman Berorientasi Objek")
dosen2.tambah_matakuliah("Kecerdasan Buatan")
dosen3.tambah_matakuliah("Embedded System")

# Mahasiswa menambahkan mata kuliah ke dalam KRS mereka
mahasiswa1.tambah_matakuliah("Pemrograman Berorientasi Objek")
mahasiswa2.tambah_matakuliah("Kecerdasan Buatan")
mahasiswa3.tambah_matakuliah("Embedded System")

# Dosen menambahkan nilai untuk mahasiswa
dosen1.tambah_nilai(mahasiswa1, "Pemrograman Berorientasi Objek", "A")
dosen2.tambah_nilai(mahasiswa2, "Kecerdasan Buatan", "B")
dosen3.tambah_nilai(mahasiswa3, "Embedded System", "B+")

# Tampilkan KRS mahasiswa
mahasiswa1.tampilkan_krs()
mahasiswa2.tampilkan_krs()
mahasiswa3.tampilkan_krs()

# Mahasiswa melihat nilai mereka
mahasiswa1.lihat_nilai()
mahasiswa2.lihat_nilai()
mahasiswa3.lihat_nilai()

# Tampilkan mata kuliah yang diajarkan oleh dosen
dosen1.tampilkan_matakuliah()
dosen2.tampilkan_matakuliah()
dosen3.tampilkan_matakuliah()
