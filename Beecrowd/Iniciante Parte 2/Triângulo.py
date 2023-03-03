a,b,c = input().split()

a = float(a)
b = float(b)
c = float(c)

peri = float(a + b + c)
area = float(((a + b) * c) /2)  
if (b-c) < a < b + c and (a-c) < b < a + c and a - b < c < a + b:
    print("Perimetro = %.1f"%peri)
else:
    print("Area = %.1f"%area)