#Leia a idade e o sexo
#Mostre opção de continualidade
#Mostre quantas pessoas acima de 18 anos
#Quantos homens cadastrados
#Quantas mulheres acima de 20 anos cadastradas
count = maior = masc = fem = 0

while True:
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    resp = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo[M/F]')).strip().upper()[0]
    count += 1
    if idade > 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if idade < 20 and sexo == 'F':
        fem += 1
    while resp not in 'SN':
        resp = str(input('Deseja continuar a cadastrar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'No nosso cadastro tem {maior} pessoas com mais de 20 anos \n E tem {fem} mulheres mais novas que 18 anos \n E tem {masc} homens cadastrados')







