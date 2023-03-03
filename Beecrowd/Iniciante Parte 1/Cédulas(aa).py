dinheiro = int(input())

print (dinheiro)

notas100 = dinheiro//100
dinheiro= dinheiro%100

notas50 = dinheiro//50
dinheiro =dinheiro%50

notas20 = dinheiro//20
dinheiro = dinheiro%20

notas10 =  dinheiro//10
dinheiro = dinheiro%10

notas05 = dinheiro//5
dinheiro = dinheiro%5

notas02 = dinheiro//2
dinheiro = dinheiro%2

print(f"{notas100} nota(s) de R$ 100,00")
print(f"{notas50} nota(s) de R$  50,00")
print(f"{notas20} nota(s) de R$  20,00")
print(f"{notas10} nota(s) de R$  10,00")
print(f"{notas05} nota(s) de R$   5,00")
print(f"{notas02} nota(s) de R$   2,00")
print(f"{dinheiro} nota(s) de R$  1,00")
