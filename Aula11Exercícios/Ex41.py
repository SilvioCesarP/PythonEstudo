#Leia o ano de nascimento do atleta
#Mostre a categoria em que se encontra

ano = int(input('Qual ano que voce nasceu? '))
idade = 2023 - ano
print('Tendo {} anos em 2023 : '.format(idade))
if idade <= 9:
    print('Voce está na categoria MIRIM')
elif idade > 9 and idade <= 14:
    print('Voce está na categoria INFANTIL!')
elif idade > 14 and idade <= 19:
    print('Você está na categoria JUNIOR')
elif idade > 19 and idade <= 25:
    print('Você está na categoria SENIOR') 
elif idade > 25:
    print('Você está na categoria MASTER!')
else:
    print('ERRO!')