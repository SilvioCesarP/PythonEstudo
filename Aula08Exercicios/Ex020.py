#Leia quatro alunos e faça uma ordem de nomes aleatorios
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
ordem = random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(ordem))