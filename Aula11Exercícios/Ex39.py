#Leia o ano de nascimento
#informe de acordo com a idade dele: se ele ainda vai se alistar no exercito, se é a hota de se alistar ou se ja passou a hora
#Mostar o tempo que falta ou o tempo que passou do prazo

ano = int(input('o ano de seu nascimento: '))
idade = 2023 - ano
novo = 18 - idade
novo2 = idade - 18
print('Sua idade é {} em 2023'.format(idade))

if idade < 18:
    print('Voce ainda vai ter que se alistar para o exercito em {} anos'.format(novo))
elif idade == 18:
    print('PARABENS ESSE ANO OU VC VAI SE ALISTAR OU JA SE ALISTOU!!!')
else:
    print('Passou seu prazo de se alistar! Cuidado faz {} anos que venceu!'.format(novo2))
