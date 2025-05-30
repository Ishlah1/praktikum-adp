def input_data():
    a=int(input("Masukkan jumlah praktikan: "))
    data=[]
    for i in range(a):
        print(f"\nPraktikan ke-{i+1}")
        nama=input("Nama: ")
        nim=input("NIM: ")
        pretest=float(input("Nilai pretest: "))
        posttest=float(input("Nilai posttest: "))
        tugas=float(input("Nilai tugas/makalah: "))
        bonus=float(input("Nilai bonus: "))
        nilai_akhir=(0.25*pretest+0.25*posttest+0.5*tugas)+bonus
        praktikan=[nama,nim,pretest,posttest,tugas,bonus,nilai_akhir,0]
        data.append(praktikan)
    return data

def rata2(data):
    total=0
    n=len(data)
    for i in range (n):
        total=total+data[i][6]
    return total/n

def peringkat(data):
    n=len(data)
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j][6]<data[j+1][6]:
                a=data[j]
                data[j]=data[j+1]
                data[j+1]=a
    for i in range(n):
        data[i][7]=i+1

def tabel(data,rata2):
    print("\n"+"_"*56)
    print("|"+"Nama".ljust(15),"|"+"NIM".ljust(8),"|"+"Nilai Akhir".ljust(15),"|"+"Peringkat".ljust(10)+"|")
    print("|"+"_"*16+"|"+"_"*9+"|"+"_"*16+"|"+"_"*10+"|")
    for i in range(len(data)):
        print("|"+data[i][0].ljust(15),"|"+data[i][1].ljust(8),"|"+str(data[i][6]).ljust(15),"|"+str(data[i][7]).ljust(10)+"|")
        print("|"+"_"*16+"|"+"_"*9+"|"+"_"*16+"|"+"_"*10+"|")
    print(f"|Rata-rata nilai akhir     |{str(rata2)}".ljust(55)+"|")
    print("|"+"_"*26+"|"+"_"*27+"|")
    
data=input_data()
rata2=rata2(data)
peringkat(data)
tabel(data,rata2)