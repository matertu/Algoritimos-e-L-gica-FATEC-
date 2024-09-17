i = int(input("inteiro = "))
print("digite números decimais = ")
f = float(input())
s = 0
while f != int:
    try:
        s = s+f
        f = float(input())
    except ValueError:
        break
print(s+i)