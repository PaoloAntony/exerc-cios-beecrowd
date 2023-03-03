horan,minn,horaf,minf = map(int,input().split())
tempo = 0
tempom = 0
if horan > horaf:
    horaf += 24
    tempo = horaf - horan
elif horan == horaf:
    tempo = 24
else:
    tempo = horaf - horan

if minn > minf:
    minf += 60
    tempom = minf - minn
elif minn == minf:
    tempom = 0
else:
    tempom = minf - minn

if tempo == 1 and tempom < 60:
    tempo = 0
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(tempo,tempom))
else:
    print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)"%(tempo,tempom))

