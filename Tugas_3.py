print ('''
Misalkan N(t) adalah variable acak Poisson dengan parameter λt > 0 sehingga:
P(N(t)=n)=e^(-λt) 〖(λt)〗^n/n!
''')

λt = float (input ("masukan nilai λt>0: "))
batas_n = int (input("masukan nilai n:"))
print (" ")
e = 2.71828
n = 0
faktorial = 1
Pn = e ** (-λt)

while batas_n >= n:
    print (f"untuk P(N(t) = {n}) = {Pn}")
    faktorial = faktorial * (n+1)
    Pn = (Pn * λt)/(n+1)
    n = n +1
