a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

sit1a = a - b
sit2a = a - c

sit1b = b - a
sit2b = b - c

sit1c = c - a
sit2c = c - b

if sit1a and sit2a > 0:
    print("%s eh o maior" %a)

elif sit1b and sit2b > 0:
    print("%s eh o maior" %b)

else:
    print("%s eh o maior"%c)