sal = float(input())
perct = 0
reaj  = 0
if sal > 0 and sal <= 400:
    reaj = sal *(15/100)
    novo = sal *(15/100) + sal 
    perct =+ 15 
elif sal > 400.01 and sal <= 800:
    reaj = sal * (12/100) 
    novo = sal * (12/100) + sal
    perct =+ 12 
elif sal >= 800.01 and sal <= 1200:
    reaj = sal * (10/100)
    novo = sal * (10/100) + sal
    perct =+ 10
elif sal >= 1200.01 and sal <= 2000:
    reaj = sal * (7/100)
    novo = sal * (7/100) + sal
    perct =+ 7  
else:
    reaj = sal * (4/100)
    novo = sal * (4/100) + sal
    perct =+ 4


print("Novo salario: %.2f"%novo)
print("Reajuste ganho: %.2f"%reaj)
print(f"Em percentual: {perct} %")