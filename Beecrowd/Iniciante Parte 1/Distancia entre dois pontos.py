import math

x1,y1 = input().split()
x2,y2 = input().split()

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

conta =((x2 - x1)**2) + ((y2 - y1)**2) 
#formula para raiz quadrada na extensão math 
raiz = math.pow (conta,1/2)
print("%.4f"%raiz)