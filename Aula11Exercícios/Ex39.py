#Leia o ano de nascimento
#informe de acordo com a idade dele: se ele ainda vai se alistar no exercito, se é a hota de se alistar ou se ja passou a hora
#Mostar o tempo que falta ou o tempo que passou do prazo

ano = int(input('o ano de seu nascimento: '))
alistamento = +(ano - 2023)
if alistamento > 18:
    print('Voce ainda vai ter que se alistar para o exercito em {} anos'.format((alistamento- 18)))
elif alistamento == 18:
    print('Você terá que se alistar esse ano, PARABENS!!')
else:
    print('Voce tem pendencias com o exercito e passou {} do prazo de alistamento'.format(alistamento- 18))