#Leia um nome
#Mostre se tem um no 'Silva' inserido no nome
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome tem Santo? {}'.format('silva' in nome.lower()))
