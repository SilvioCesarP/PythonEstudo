#Leia o peso de 5 pessoas
# mostre qual delas é o meior e qual é o menor peso
pesomaior = 0
pesomenor = 0
for ps in range(1,6):
    peso = float(input('Qual é o {}º peso? '.format(ps)))
    if ps == 1:
        pesomaior = peso
        pesomenor = peso
    else:
        if peso > pesomaior:
            pesomaior = peso
        elif peso < pesomenor:
            pesomenor = peso

print('o peso maior é {:.2f} e o menor é {:.2f}'.format(pesomaior, pesomenor))


