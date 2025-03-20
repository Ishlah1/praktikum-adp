print ('''
Misalkan N(t) adalah variable acak Poisson dengan parameter λt > 0 sehingga:
P(N(t)=n)=e^(-λt) 〖(λt)〗^n/n!
''')

λt = float (input ("masukan nilai λt>0: "))
batas_n = int (input("masukan nilai n:"))
print (" ")
e = 2.71828
n = 0

while batas_n >= n:
    N = 1
    i = 1
    while i <= n:
        N = N * i
        i = i + 1
    if n == 0:
        n = 1
    Pn = (e**-λt) * (λt**n) / N
    print (f"untuk P(N(t) = {n}) = {Pn}")
    n = n + 1   