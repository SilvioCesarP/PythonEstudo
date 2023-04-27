#Leia o nome, idade e sexo de 4 pessoas
#Mostre a média do grupo(idade), quem é o homem mais velho, quantas mulheres tem menos de 20 anos
count = 0
maior = 0
menor = 0
nomemaior = ''
soma = 0
somam = 0
media = 0

for ct in range(1,5):
    nome = str(input('Qual é o nome da {}º pessoa? '.format(ct))).strip().title()
    idade = float(input('Qual é a sua idade {}? '.format(nome)))
    sexo = str(input('Qual é o seu sexo, {}?[F] ou [M]? '.format(nome))).strip().upper()
    count += idade
    media = count / ct
    if sexo == 'M' or 'MASCULINO':
        if ct == 1:
            maior = idade
            menor = idade
            nomemaior = nome
        elif ct > 1:
            if idade > maior:
                idade = maior
                nomemaior = nome
            elif idade < maior:
                idade = menor
        else:
            print('Digite apenas a letra M ou F ou Masculino e Feminino')
    elif sexo == 'F' or 'FEMININO':
        if idade < 20:
            soma += 1
        else:
            somam = 1

print('A média do grupo é {:.2f} o nome do homem mais velho é {} com {}e tem {} mulheres mais velhas que 20 anos'.format(media, maior, nomemaior, soma))
            
        







