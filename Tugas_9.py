import random
from termcolor import colored

# Fungsi untuk membuat parkiran bernomor
def buat_parkiran(baris, kolom):
    nomor = 1
    return [[(nomor := nomor + 1) - 1 if random.choice([True, False]) else 0 for _ in range(kolom)] for _ in range(baris)]

# Parkiran
parkiran_mobil_truk = buat_parkiran(4, 6)  # Lantai 1
parkiran_motor = buat_parkiran(3, 8)       # Lantai 2

def tampilkan_parkiran(parkiran):
    nomor_slot = 1
    for baris in parkiran:
        for slot in baris:
            nomor_str = f"{nomor_slot:02}"
            if slot:  # Slot terisi
                print(colored(f"[{nomor_str}]", "white", "on_red"), end=" ")
            else:     # Slot kosong
                print(colored(f"[{nomor_str}]", "white", "on_green"), end=" ")
            nomor_slot += 1
        print()

def main():
    print("=== SISTEM MANAJEMEN PARKIRAN ===")
    print("Pilih jenis kendaraan:")
    print("1. Mobil")
    print("2. Motor")
    print("3. Truk")

    pilihan = input("Masukkan pilihan (1-3): ")

    if pilihan == "1":
        kendaraan = "Mobil"
        lantai = 1
        parkiran = parkiran_mobil_truk
    elif pilihan == "2":
        kendaraan = "Motor"
        lantai = 2
        parkiran = parkiran_motor
    elif pilihan == "3":
        kendaraan = "Truk"
        lantai = 1
        parkiran = parkiran_mobil_truk
    else:
        print(colored("Pilihan tidak valid!", "red"))
        return

    print(f"\nKendaraan: {kendaraan}")
    print(f"Diarahkan ke Lantai {lantai}")
    print("Tampilan Parkiran:\n")
    print("Merah : Terisi"" \n""Hijau : Kosong")
    tampilkan_parkiran(parkiran)

if __name__ == "__main__":
    main()