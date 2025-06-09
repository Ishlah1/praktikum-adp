mjk="data_manajemen_keuangan.txt"

def baca_data():
    data=[]
    file=open(mjk,"r")
    for i in file:
        bagian=i.split("_")
        if len(bagian)==4:
            data.append({
                "tanggal":bagian[0],
                "keterangan":bagian[1],
                "nominal":int(bagian[2]),
                "tipe":bagian[3]
            })
    file.close()
    return data

def simpan_data(data):
    file=open(mjk,"w")
    for i in data:
        file.write(i["tanggal"]+"_"+i["keterangan"]+"_"+str(i["nominal"])+"_"+i["tipe"]+"_"+"\n")
    file.close()

def tambah_data(data):
    print("\n"+"=====Tambah Data Keuangan=====")
    tanggal=input("tanggal-bulan-hari (05-06-2025): ")
    tipe=input("tipe transaksi (pemasukan/pengeluaran): ")
    if tipe != "pemasukan" and tipe != "pengeluaran":
        print("Tipe tidak ada")
        return
    keterangan=input("Keterangan: ")
    nominal=int(input("nominal (15000): "))
    data.append({
        "tanggal":tanggal,
        "keterangan":keterangan,
        "nominal":nominal,
        "tipe":tipe,
    })
    simpan_data(data)
    print("Data berhasil ditambahkan!")

def tampilkan_data(data):
    print("\n===Data Keuangan===")
    if len(data)==0:
        print("Belum ada data")
    else:
        for i in range(len(data)):
            item=data[i]
            print(str(i+1)+". [" + item["tanggal"] + "] "+item["keterangan"]+" - Rp"+str(item["nominal"])+" (" +item["tipe"]+')')

def hapus_data(data):
    tampilkan_data(data)
    if len(data)==0:
        return
    nomor=int(input("Masukkan nomor data yang ingin dihapus: "))
    if 1<=nomor<=len(data):
        dihapus=data.pop(nomor-1)
        simpan_data(data)
        print("Data '"+dihapus["keterangan"]+"' berhasil dihapus.")
    else:
        print("Nomor tidak ada")

def menu():
    file=open(mjk,"a")
    file.close()
    data=baca_data()
    while True:
        print('''
=====Mnajemen Keuangan=====
1. Tambah data keuangan
2. Hapus data keuangan
3. Tampilkan semua data
4. Keluar''')
        pilih=input("Pilih (1/2/3/4): ")
        if pilih=="1":
            tambah_data(data)
        elif pilih=="2":
            hapus_data(data)
        elif pilih=="3":
            tampilkan_data(data)
        elif pilih=="4":
            print("Terimakasih")
            break
        else:
            print("Pilihan tidak ada")
menu()
