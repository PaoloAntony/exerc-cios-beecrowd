pares= 0
impares= 0
positivos = 0
negativos = 0

for x in range(5):
    numeros = int(input())
    if numeros > 0:
       positivos += 1
    elif numeros < 0:
        negativos += 1

    if numeros %2 == 0:
        pares += 1
    else:
        impares += 1

print ("%d valor(es) par(es)"%pares)
print ("%d valor(es) impar(es)"%impares)
print ("%d valor(es) postivo(s)"%positivos)
print ("%d valor(es) negativo(s)"%negativos)