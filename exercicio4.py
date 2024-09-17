i = int(input("inteiro = "))
print("digite números decimais = ")
f = float(input())
s = 0
while f != int and f > 0:
    try:
        if f > 0:
            s = s+f
        else:
            pass
        f = float(input())
    except ValueError:
        break
print(s+i)