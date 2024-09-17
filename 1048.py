s = float(input())
if s <= 400:
    r = 0.15
elif 400 < s <= 800:
    r = 0.12
elif 800 < s <= 1200:
    r = 0.10
elif 1200 < s <= 2000:
    r = 0.07
elif s > 2000:
    r = 0.04
if s > 0:
    print(f"Novo salario: {s*(1+r):.2f}\nReajuste ganho: {s*r:.2f}\nEm percentual: {r*100:.0f} %")

