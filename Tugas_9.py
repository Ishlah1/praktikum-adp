import os as a
import time as t
from termcolor import cprint as warna

j=0
gelombang=[0,1,2,3,4,3,2,1]

def hapus():
    a.system('cls')

def tiang_bendera(j):
    for i in range(1):
        for k in range(4):
            y=(j+k)%len(gelombang)
            x=gelombang[y]
            print("   ",end='')
            warna ("|", "dark_grey","on_dark_grey", end="")
            warna(" "*x+" "*25, "red", "on_red")
    for i in range(1):
        for k in range(4):
            y=(4+j+k)%len(gelombang)
            x=gelombang[y]
            print("   ",end='')
            warna ("|", "dark_grey","on_dark_grey", end="")
            warna(" "*x+" "*25, "white", "on_white")
    for i in range(10):
        print("   ",end='')
        warna ("|", "dark_grey","on_dark_grey")
    print("  ",end="")
    warna ("   ","dark_grey","on_dark_grey")
    warna ("       ","dark_grey","on_dark_grey")
    
while True:
    hapus()
    tiang_bendera(j)
    j+=1  
    t.sleep(0.08)
