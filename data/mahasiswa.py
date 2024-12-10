class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"{self.nim} - {self.nama} - {self.jurusan}"


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self, mahasiswa):
        self.data.append(mahasiswa)

    def hapus(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah(self, nim, nama=None, jurusan=None):
        for m in self.data:
            if m.nim == nim:
                if nama:
                    m.nama = nama
                if jurusan:
                    m.jurusan = jurusan
                break

    def cari(self, nim):
        for m in self.data:
            if m.nim == nim:
                return m
        return None

    def daftar(self):
        return self.data
