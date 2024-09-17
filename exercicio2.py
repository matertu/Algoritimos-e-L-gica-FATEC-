a = True
p = 0
n = 0
print("Digite quaisquer números inteiros. Para encerrar a operação digite 0: ")
while a:
    x = int(input())
    if x > 0:
        p = p + x
    elif x < 0:
        n = n + x
    else:
        a = False
        print(f'A Soma dos valores positivos é igual a: {p}\nA Soma dos valores negativos é igual a: {n}')

