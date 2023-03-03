com,fin = map(int,input().split())

if com > fin:
    fin += 24
    tempo = fin - com
elif com == fin:
    tempo = 24
else:
    tempo = fin - com 

print("O JOGO DUROU %d HORA(S)"%tempo)
