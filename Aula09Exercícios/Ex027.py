#Leia um nome
#Mostre o primeiro nome e o ultimo separadamente
nome = str(input('Digite seu nome: ')).strip().title()
n = nome.split()
print('O seu primeiro nome é {}'.format(n[0]))
print('O seu ultimo nome é: {}'.format(n[len(n) - 1]))