while True:
    titik = []
    n = input("masukan jumlah titik: ")
    if n>'0':
        n=int(n)
        for i in range(n):
            print(f"\ntitik ke-{i+1}")
            x = float(input("nilai x: "))
            y = float(input("nilai y: "))
            titik.append([x, y])
        print("\ndaftar titik:")
        for i in range(n):
            print(f"titik ke-{i+1} = ({str(titik[i][0])}, {str(titik[i][1])})")
        print()
        for i in range(n):
            for j in range(i+1, n):
                Tx = titik[i][0] - titik[j][0]
                Ty = titik[i][1] - titik[j][1]
                jarak = (Tx**2 + Ty**2) ** 0.5
                print(f"Jarak titik {str(i+1)} ke titik {str(j+1)} = {str(jarak)}")
        break
    elif n<='0':
        print("masukan angka >0")