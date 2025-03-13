print ('''
================DAFTAR PAKET BUKA PUASA==================
________________________________________________________
| PAKET |                 ISI                |   HARGA  |
|_______|____________________________________|__________|
|   A   |Nasi goreng Spesial  + Es Teh       |Rp 15.000 |
|_______|____________________________________|__________|
|   B   |Nasi + Ayam Goreng + Tahu + Tempe   |Rp 17.000 |
|_______|____________________________________|__________|
|   C   |Nasi + Ayam Bakar + Tahu + Tempe    |Rp 20.000 |
|_______|____________________________________|__________|
|   D   |Nasi + Soto                         |Rp 15.000 |
|_______|____________________________________|__________|
|   E   |Mie Nyemek + Es Teh                 |Rp 12.000 |
|_______|____________________________________|__________|
|   F   |Nasi + Ayam Geprek + Teh            |Rp 13.000 |
|_______|____________________________________|__________|

*harga makanan belum termasuk pajak 10%
*gratis ongkir untuk minimum pembelian Rp 150.000
=========================================================
''')

nama = input ("Pesanan atas nama: ")
no_tlp = int(input (f"baik {nama}, masukan nomor telepon anda: +62"))
almt_pngrmn = input ("masukan lokasi pengiriman: ")
pkt_dplh = input ("silahakn pilih paket: ").upper() 

if pkt_dplh == "A":
    harga = 15000
    menu = "Nasi goreng Spesial  + Es Teh"
elif pkt_dplh == "B":
    harga = 17000
    menu = "Nasi + Ayam Goreng + Tahu + Tempe"
elif pkt_dplh == "C":
    harga = 20000
    menu = "Nasi + Ayam Bakar + Tahu + Tempe"
elif pkt_dplh == "D":
    harga = 15000
    menu = "Nasi + Soto"
elif pkt_dplh == "E":
    harga = 12000
    menu = "Mie Nyemek + Es Teh"
elif pkt_dplh == "F":
    harga = 13000
    menu = "Nasi + Ayam Geprek + Teh"

jmlh_pkt = int(input ("jumlah paket yang ingin dibeli: "))
ttl_hrg = harga * jmlh_pkt
pajak = ttl_hrg * 0.1

if ttl_hrg < 150000 :
    biaya_pengiriman = 25000
else:
    biaya_pengiriman = 0
ttl_akhr = ttl_hrg + pajak + biaya_pengiriman

print(f'''
====================STRUK PEMESANAN======================
Nama                :{nama}
No Telepon          :+62{no_tlp}
Alamat Pengiriman   :{almt_pngrmn}
Detail Pesanan      :{menu}

---------------------------------------------------------
Harga Satuan        :Rp {harga}        x{jmlh_pkt}
Total Harga         :Rp {ttl_hrg}
Pajak (10%)         :Rp {pajak}
Biaya Pengiriman    :Rp {biaya_pengiriman}
                    ----------------------- +
Total Akhir         :Rp {ttl_akhr}

======================Terima Kasih=======================
''')