buku = {
    "judul" : "dasar pemrograman",
    "penulis" : "someone",
    "tahun_terbit" : 1999
}

while True:
    print("======MENU======")
    print("1. Tampilkan data")
    print("2. Tambah data penerbit")
    print("3. Ubah data penulis")
    print("4. Hapus data penerbit")
    print("5. Selesai")

    pilihan = input("Pilih menu(1-5): ")
    if pilihan == "1":
        print("--------------------------")
        print("Judul : ", buku["judul"])
        print("Penulis : ", buku["penulis"])
        print("Tahun Terbit : ", buku["tahun_terbit"])
        print("Penerbit : ", buku.get("penerbit", "Belum ada data"))
        pass

    elif pilihan == "2":
        penerbit = input("Masukkan nama penerbit: ")
        buku["penerbit"] = penerbit
        print("Data penerbit berhasil ditambahkan")

    elif pilihan == "3":
        penulis = input("Nama penulis baru: ")
        buku["penulis"] = penulis
        print("Data berhasil diubah")

    elif pilihan == "4":
        buku.pop("penerbit", None)
        print("Data penerbit berhasil dihapus")

    elif pilihan == "5":
        print("Program Selesai")
        break

    else:
        print("Pilihan tidak valid, silahkan pilih nomor 1 - 5!")

