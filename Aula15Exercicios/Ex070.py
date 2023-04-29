#leia o nome e o preço de produtos
#Mostre se quer continuar ou não
#No termino mostrar o gasto total
#Quantos produtos custaram mais de 1000
#E qual foi o produto mais barato
soma = maior = barato = count = 0
produto = ' '

while True:
    nome = str(input('Digite o que quer comprar: ')).strip()
    valor = float(input('Digite o valor do produto: R$'))
    print('=-'*10)
    print('COMPRA COMFIRMADA!!!')
    print('=-'*10)
    soma += valor
    count += 1
    if count == 1:
        barato = valor
    elif valor <= barato:
        barato = valor
        produto = nome

    if valor > 1000:
        maior += 1
    
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar a fazer suas compras?[S/N] ')).strip().upper()[0]
        print('=-'*10)
    if resp == 'N':
        break
print(f'Total gasto nas compras {soma}\nA quantidade de produtos com o valor maior que R$1000 é {maior}\nO produto mais barato foi {produto} de {barato}')

    
