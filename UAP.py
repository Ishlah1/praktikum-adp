import os
import time
from datetime import datetime
from termcolor import colored

# File penyimpanan
DATA_FILE = "data_kendaraan.txt"
PENDAPATAN_FILE = "pendapatan_harian.txt"
PARKIRAN_FILE = "data_parkiran.txt"

# Fungsi membuat layout parkiran kosong
def buat_parkiran(baris, kolom):
    return [[0 for _ in range(kolom)] for _ in range(baris)]

# Load parkiran dari file
if os.path.exists(PARKIRAN_FILE):
    with open(PARKIRAN_FILE, "r") as f:
        lines = f.readlines()
        parkiran = {"lantai_1": [], "lantai_2": []}
        lantai = "lantai_1"
        for line in lines:
            if line.strip() == "lantai_2":
                lantai = "lantai_2"
                continue
            parkiran[lantai].append([int(x) for x in line.strip().split()])
else:
    parkiran = {
        "lantai_1": buat_parkiran(3, 3),
        "lantai_2": buat_parkiran(4, 5)
    }

# Load kendaraan dari file
data_kendaraan = {}
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        for line in f:
            bagian = line.strip().split(",")
            if len(bagian) == 3:
                key, jenis, waktu_str = bagian
                data_kendaraan[key] = {
                    "jenis": jenis,
                    "waktu_masuk": datetime.strptime(waktu_str, "%Y-%m-%d %H:%M:%S")
                }

# Load pendapatan
pendapatan_harian = 0
if os.path.exists(PENDAPATAN_FILE):
    with open(PENDAPATAN_FILE, "r") as f:
        try:
            pendapatan_harian = int(f.read().strip())
        except:
            pendapatan_harian = 0

# Simpan semua data
def simpan_data():
    with open(DATA_FILE, "w") as f:
        for key, val in data_kendaraan.items():
            f.write(f"{key},{val['jenis']},{val['waktu_masuk'].strftime('%Y-%m-%d %H:%M:%S')}\n")
    with open(PENDAPATAN_FILE, "w") as f:
        f.write(str(pendapatan_harian))
    with open(PARKIRAN_FILE, "w") as f:
        for lantai in ["lantai_1", "lantai_2"]:
            for row in parkiran[lantai]:
                f.write(" ".join(str(x) for x in row) + "\n")
            if lantai == "lantai_1":
                f.write("lantai_2\n")

def tampilkan_parkiran():
    os.system('cls')
    print("\n========== LAYOUT PARKIRAN ==========\n")
    for lantai in parkiran:
        print(f"{lantai.upper()} ({'Mobil/Truk' if lantai == 'lantai_1' else 'Motor'})")
        nomor = 1
        for baris in parkiran[lantai]:
            for slot in baris:
                warna = "on_red" if slot else "on_green"
                print(colored(f"[{nomor:02}]", "white", warna), end=" ")
                nomor += 1
            print()
    print("====================================\n")

def animasi(text):
    for i in range(10):
        os.system('cls')
        print(" "*(10-i)+f"🏍️🚛🚗 {text}"+"."*(i))
        time.sleep(0.05)

def struk_masuk(lantai, slot, jenis, waktu):
    print(f"""
    ========= STRUK MASUK =========
    Kendaraan   : {jenis.upper()}
    Lantai      : {lantai.upper()}
    Slot        : {slot}
    Waktu Masuk : {waktu.strftime('%Y-%m-%d %H:%M:%S')}
    ===============================
    """)
    input("Tekan Enter untuk lanjut...")

def struk_keluar(lantai, slot, data):
    global pendapatan_harian
    keluar = datetime.now()
    masuk = data['waktu_masuk']
    durasi = keluar - masuk
    jam = max(1, durasi.seconds // 3600)
    tarif = {"motor": 3000, "mobil": 5000, "truk": 12000}
    total = jam * tarif[data['jenis']]
    pendapatan_harian += total

    print(f"""
    ========= STRUK KELUAR =========
    Kendaraan   : {data['jenis'].upper()}
    Lantai      : {lantai.upper()}
    Slot        : {slot}
    Waktu Masuk : {masuk.strftime('%Y-%m-%d %H:%M:%S')}
    Waktu Keluar: {keluar.strftime('%Y-%m-%d %H:%M:%S')}
    Durasi Parkir: {jam} jam
    Tarif        : Rp {tarif[data['jenis']]:,} / jam
    Total Bayar  : Rp {total:,}
    ================================
    """)
    input("Tekan Enter untuk lanjut...")

def laporan():
    print(f"\nTotal pendapatan hari ini: Rp {pendapatan_harian:,}")
    time.sleep(3)

# Program utama
while True:
    tampilkan_parkiran()
    print("1. Masuk Parkir\n2. Keluar Parkir\n3. Lihat Pendapatan\n4. Keluar Program")
    pilihan = input("Pilih menu: ")

    if pilihan == "4":
        simpan_data()
        print("✅ Data disimpan. Program keluar.")
        break

    elif pilihan == "1":
        tampilkan_parkiran()
        jenis_map = {"1": "motor", "2": "mobil", "3": "truk"}
        jenis_input = input("Jenis (1. Motor, 2. Mobil, 3. Truk): ")
        if jenis_input not in jenis_map:
            print("❌ Jenis tidak valid.")
            continue
        jenis = jenis_map[jenis_input]
        lantai = "lantai_2" if jenis == "motor" else "lantai_1"
        try:
            slot = int(input("Pilih slot: "))
            i, j = divmod(slot - 1, len(parkiran[lantai][0]))
            if parkiran[lantai][i][j] == 1:
                print("❌ Slot sudah terisi.")
                continue
            animasi("Masuk Parkiran")
            parkiran[lantai][i][j] = 1
            waktu = datetime.now()
            struk_masuk(lantai, slot, jenis, waktu)
            data_kendaraan[f"{lantai}_{slot}"] = {"jenis": jenis, "waktu_masuk": waktu}
        except:
            print("❌ Input tidak valid.")

    elif pilihan == "2":
        tampilkan_parkiran()
        lantai_input = input("Lantai (1 atau 2): ")
        lantai = "lantai_1" if lantai_input == "1" else "lantai_2"
        try:
            slot = int(input("Nomor slot: "))
            i, j = divmod(slot - 1, len(parkiran[lantai][0]))
            key = f"{lantai}_{slot}"
            if parkiran[lantai][i][j] == 0 or key not in data_kendaraan:
                print("❌ Tidak ada kendaraan di slot ini.")
                continue
            animasi("Keluar Parkiran")
            struk_keluar(lantai, slot, data_kendaraan[key])
            parkiran[lantai][i][j] = 0
            del data_kendaraan[key]
        except:
            print("❌ Input tidak valid.")

    elif pilihan == "3":
        laporan()

    else:
        print("❌ Menu tidak tersedia.")
