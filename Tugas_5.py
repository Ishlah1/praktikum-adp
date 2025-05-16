NIM = []
NAMA = []
NILAI = []

while True:
    print('''MANAJEMEN NILAI MAHASISWA
    1. Tambah Data
    2. Hapus Data
    3. Tampilkan Data
    4. Keluar''')
    opsi = input("Pilih opsi (1-4): ")
    if opsi == "1":
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ").upper()
        nilai = float(input("Masukkan Nilai: "))
        NIM.append(nim)
        NAMA.append(nama)
        NILAI.append(nilai)
        print("Data berhasil ditambahkan")
    elif opsi == "2":
        hapus = input("Masukkan NIM yang ingin dihapus: ")
        if hapus in NIM:
            index = NIM.index(hapus)
            A = []
            B = []
            C = []

            for i in range(len(NIM)):
                if i != index:
                    A.append(NIM[i])
                    B.append(NAMA[i])
                    C.append(NILAI[i])
            NIM = A
            NAMA = B
            NILAI = C
            print("Data dihapus")
        else:
            print("NIM tidak ditemukan")
    elif opsi == "3":
        if not NIM:
            print("Belum ada data")
        else:
            for i in range(len(NILAI)):
                for j in range(0, len(NILAI) - i - 1):
                    if NILAI[j] < NILAI[j + 1]:
                        a = NILAI[j]
                        b = NIM[j]
                        c = NAMA[j]

                        NILAI[j] = NILAI[j + 1]
                        NIM[j] = NIM[j + 1]
                        NAMA[j] = NAMA[j + 1]

                        NILAI[j + 1] = a
                        NIM[j + 1] = b
                        NAMA[j + 1] = c
            print("\nData Mahasiswa dari urutan tertinggi:")
            for i in range(len(NIM)):
                print(f"NIM: {NIM[i]}, Nama: {NAMA[i]}, Nilai: {NILAI[i]}")
    elif opsi == "4":
        print("program selesai")
        break
    else:
        print("pilihan tidak valid, coba lagi.")