s = float(input())
if s > 0:
    if 0 < s <= 2000:
        print("Isento")
    elif 2000 < s <= 3000:
        t = 0.08
        df = s-2000.01
        print(f"R$ {df * t:.2f}")
    elif 3000 < s <= 4500:
        t = 0.18
        df = s-3000.01
        print(f"R$ {df * t + 80:.2f}") #a soma equivale ao valor calculado da tese anterior
    else:
        t = 0.28
        df = s-4500.01
        print(f"R$ {df * t + 350:.2f}") #a soma equivale ao valor calculado da tese anterior