#Leia o primeiro termo
#Leia a razão
#Mostre uma PA em 10 termos
#De opção de acrescentar termos até que o usuario digite 0

print('GERADOR DE PA')
print('=-'*20)
num = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
count = 1
termo = num
total = 0
mais = 10

while mais != 0:
    total += mais
    while count <= total:
        print(termo, end=' -> ')
        count += 1
        termo += razao
    mais = int(input('Insira novo valor para quantidade de termos: '))
print(f'Terminou, a contagem de vezes do termo é {count - 1}')