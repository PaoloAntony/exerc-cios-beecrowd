escolha,vezes  = input().split()

escolha = int(escolha)
vezes  = int(vezes)

if escolha == 1:
    escolha = 4.00
elif escolha == 2:
    escolha = 4.50
elif escolha == 3:
    escolha = 5.00
elif escolha == 4:
    escolha = 2.00
else:
    escolha = 1.5

total = escolha*vezes  
total = float(total)

print("Total: R$ %.2f"%total)