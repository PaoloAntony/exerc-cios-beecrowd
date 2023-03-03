diac = int(input("Dia "))
hc,mc,sc = map(int,input().split(":"))
diaf = int(input("Dia "))
hf,mf,sf = map(int,input().split(":"))

tempodias = diaf - diac -1 
minutos = mf - mc 
segundos = sf - sc
tempo = 0
if hc > hf:
    hf += 24
    horas = hf - hc
elif hc == hf:
    horas = 24
else:
    horas = hf - hc 
if horas == 0 and minutos == 0 and segundos == 0:
    tempodias =- 1

print ("%d dia(s)"%tempodias)
print ("%d hora(s)"%horas)
print ("%d minuto(s)"%minutos)
print ("%d segundo(s)"%segundos)
