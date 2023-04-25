#leia um nome completo
#Mostre o nome com todas as letras maiúsculas
#Mostre o nome com todas as letras minúsculas
#Mostre quantas letras ao todo(sem considerar espaços)
#Mostre quantas letras tem o primeiro nome do nome completo

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome completo em letras maiúscula é {} '.format(nome.upper()))
print('Seu nome completo em letras minúsculas é {} '.format(nome.lower()))
print('A quantidade de letras do seu nome completo é: {}'.format(len(nome) - nome.count(' ')))
x = nome.split()
print('O numero de letras do seu nome é {} '.format(len(x[0])))