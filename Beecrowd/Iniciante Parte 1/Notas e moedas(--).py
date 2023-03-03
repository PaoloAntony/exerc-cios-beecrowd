dinheiro = float(input())
nota100 = 0
nota50  = 0
nota20  = 0
nota10  = 0
nota5   = 0
nota2   = 0
nota1   = 0
nota050 = 0
nota025 = 0
nota010 = 0
nota05  = 0
nota01  = 0

while dinheiro >= 100:
    dinheiro -= 100
    nota100 +=1

while dinheiro >= 50:
    dinheiro -= 50
    nota50 += 1

while dinheiro >= 20:
    dinheiro -= 20
    nota20 += 1

while dinheiro >= 10:
    dinheiro -= 10
    nota10 += 1

while dinheiro >= 5:
    dinheiro -= 5
    nota5 += 1

while dinheiro >= 2:
    dinheiro -= 2
    nota2 += 1

while dinheiro >= 1:
    dinheiro -= 1
    nota1 += 1

while dinheiro >= 0.50:
    dinheiro -= 0.50
    nota050 += 1

while dinheiro >= 0.25:
    dinheiro -= 0.25
    nota025  += 1

while dinheiro >= 0.10:
    dinheiro -= 0.10
    nota010  += 1

while dinheiro >= 0.05:
    dinheiro -= 0.05
    nota05  += 1


while dinheiro >= 0.01:
    dinheiro -= 0.01
    nota01  += 1


print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{nota1} moeda(s) de R$ 1.00")
print(f"{nota050} moeda(s) de R$ 0.50")
print(f"{nota025} moeda(s) de R$ 0.25")
print(f"{nota010} moeda(s) de R$ 0.10")
print(f"{nota05} moeda(s) de R$ 0.05")
print(f"{nota01} moeda(s) de R$ 0.01")