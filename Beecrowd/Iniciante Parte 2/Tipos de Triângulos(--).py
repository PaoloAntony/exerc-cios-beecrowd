a,b,c=map(float,input().split())

lista =[a,b,c]
lista = sorted(lista,reverse=True)

val1 = lista.pop(0) 
val2 = lista.pop(0)
val3 = lista.pop(0)

if val1 >= (val2 +val3):
    print("NAO FORMA TRIANGULO")    
if (val1**2) == (val2**2) + (val3**2):
     print("TRIANGULO RETANGULO") 

if val1 >5 and val2 > 4 and val3 > 3 and (val1**2)>(val2**2) +(val3**2):
    print("TRIANGULO OBTUSANGULO")

if (val1**2) < (val2**2) + (val3**2):
     print("TRIANGULO ACUTANGULO")

if val1 == val3 and val3 == val2 :
    print("TRIANGULO EQUILATERO")

if val1 == val2 and val1 != val3 or val2 == val3 and val3 !=val1 or val3 == val1 and val2 != val1 :
    print("TRIANGULO ISOSCELES")



    