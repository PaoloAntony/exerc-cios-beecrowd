contador = 0
soma = 0
for x in range(6):
    valor = float(input())
    if valor > 0:
        contador += 1
        soma += valor
media = soma / contador         

print(contador, "valores positivos")
print("%.1f" %media)
