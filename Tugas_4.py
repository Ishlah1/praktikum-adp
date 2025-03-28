m = 20
n = 2
hrg_vvip = 1000000
hrg_vip = 500000
hrg_reguler = 250000
hrg_ekonomi = 100000

total_kursi = m * n

kursi_vvip_akhir = n * 2
kursi_vip_akhir = n * 5
kursi_reguler_akhir = n * 15
sisa_vvip = kursi_vvip_akhir
sisa_vip = kursi_vip_akhir - kursi_vvip_akhir
sisa_reguler = kursi_reguler_akhir - kursi_vip_akhir
sisa_ekonomi = total_kursi - kursi_reguler_akhir

nomor_kursi = 1
for i in range(m):
    for j in range(n):
        print(nomor_kursi, end=" ")  
        nomor_kursi = nomor_kursi+1
    print() 

print(f'''
Harga Tiket:
VVIP: Rp.{hrg_vvip} (2 baris pertama)
VIP: Rp.{hrg_vip} (baris 3, 4, dan 5)
Reguler: Rp.{hrg_reguler}(10 baris berikutnya)
Ekonomi: Rp.{hrg_ekonomi} (sisa baris lainnya)
''')
kursi_dipesan = ""
jumlah_tiket = int(input("Masukkan jumlah tiket yang ingin dipesan: "))
i = 0
while i < jumlah_tiket:
    print(f"Pemesanan ke-{i+1}:")
    nama = input("Masukkan nama Anda: ")
    nomor_kursi = (input("Masukkan nomor kursi yang ingin dipesan: "))
    password = input("Buat password untuk akses konser: ")
    kursi_dipesan= kursi_dipesan + nomor_kursi + ", "
    nomor_kursi = int (nomor_kursi)
    if nomor_kursi <= 4:
        kategori = "VVIP"
        harga = hrg_vvip
        sisa_vvip = sisa_vvip-1
    elif 5 <= nomor_kursi <= 10:
        kategori = "VIP"
        harga = hrg_vip
        sisa_vip = sisa_vip-1
    elif 11 <= nomor_kursi <= 30:
        kategori = "Reguler"
        harga = hrg_reguler
        sisa_reguler = sisa_reguler-1
    else:
        kategori = "Ekonomi"
        harga = hrg_ekonomi
        sisa_ekonomi = sisa_ekonomi - 1
    
    print(f'''
    _______________struk pemesanan_______________
    Nama        : {nama}
    Nomor kursi : {nomor_kursi}
    Kategori    : {kategori}
    Harga       : Rp. {harga}
    Password    : {password}
    ______________________________________________''')
    i = i+1

# print(f"{kursi_dipesan}")

 
print(f'''
sisa kursi sekarang
VVIP    : {sisa_vvip}
VIP     : {sisa_vip}
Reguler : {sisa_reguler}
Ekonomi : {sisa_ekonomi}
''')

nomor_kursi = 1
for i in range(m):
    for j in range(n):
        if str(nomor_kursi) in kursi_dipesan:
            print ("0", end =" ")
        else:
            print(nomor_kursi, end=" ")
        nomor_kursi = nomor_kursi+1
    print() 
print("terimakasih telah memesan")