peca1= input().split()
peca2= input().split()

codp1,nump1,valo1 = peca1
codp2,nump2,valo2 = peca2

total1= int(nump1)*float(valo1)
total2= int(nump2)*float(valo2)
pagar = total1 + total2

print("VALOR A PAGAR: R$ %.2f"%pagar)