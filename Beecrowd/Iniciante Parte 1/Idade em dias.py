valor = int(input())

ano = valor//365

mes = (valor - (ano * 365)) //30

dias = (valor - (ano *365)-(mes*30))


print (f"{ano} ano(s)")
print (f"{mes} mes(es)")
print (f"{dias} dia(s)")



