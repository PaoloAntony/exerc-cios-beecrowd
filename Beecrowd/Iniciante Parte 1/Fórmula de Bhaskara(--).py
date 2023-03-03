import math

A,B,C = input().split()

A = float(A)
B = float(B)
C = float(C)

delta = (B*B) - (4*A*C)
if delta < 0:
    print("Impossivel calcular")
else:
    raiz = math.sqrt(delta) 
    bhas1 = ((-1* B) + raiz)
    bhas2 = ((-1* B) - raiz)

    if bhas1 > 0 or bhas2 > 0:
        print("Impossivel Calcular")    
    else:
        bhas1 = bhas1/(2*A)
        bhas2 = bhas2/(2*A)        
        print("R1 = %.5f"%bhas1)
        print("R2 = %.5f"%bhas2)



