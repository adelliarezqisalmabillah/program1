class TampilMahasiswa:
    @staticmethod
    def tampilkan_daftar(data):
        if not data:
            print("Tidak ada data mahasiswa.")
        else:
            print("Daftar Mahasiswa:")
            for m in data:
                print(m)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("Detail Mahasiswa:")
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan.")
