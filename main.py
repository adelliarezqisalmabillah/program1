from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import TampilMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Data Mahasiswa")
        print("2. Hapus Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Cari Data Mahasiswa")
        print("5. Tampilkan Daftar Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_data()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah(mahasiswa)
            print("Data berhasil ditambahkan.")
        elif pilihan == "2":
            nim = input("Masukkan NIM yang akan dihapus: ")
            data_mahasiswa.hapus(nim)
            print("Data berhasil dihapus.")
        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan diubah: ")
            nama = input("Masukkan nama baru (kosongkan jika tidak diubah): ")
            jurusan = input("Masukkan jurusan baru (kosongkan jika tidak diubah): ")
            data_mahasiswa.ubah(nim, nama, jurusan)
            print("Data berhasil diubah.")
        elif pilihan == "4":
            nim = input("Masukkan NIM yang dicari: ")
            mahasiswa = data_mahasiswa.cari(nim)
            TampilMahasiswa.tampilkan_detail(mahasiswa)
        elif pilihan == "5":
            TampilMahasiswa.tampilkan_daftar(data_mahasiswa.daftar())
        elif pilihan == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
