n = int(input("N = "))
p = int(input("P = "))
r = int(input("R = "))
x = 0
s = int(p*((r**n)-1)/(r-1))
while x < n:
 n = n - 1
 print(p)
 p = p*r
print(f'Valor da Soma = {s}')

