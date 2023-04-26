#leio o preço
#leia a forma de pagamento
#Calcule o preço de acordo com a categoria escolhida
#mostre o resultado das compras

print('=-' * 5, 'LOJA DO JOAO PÃO', '-=' * 5)
saldo = float(input('Digite o valor que gastará nas compras: '))
print('''ESCOLHA UMA FORMA DE PAGAMENTO; 
[ 1 ] A VISTA NO DINHERIO/ CHEQUE: 10% DE DESCONTO;
[ 2 ] A VISTA NO CARTÃO: 5% DE DESCONTO;
[ 3 ] EM ATÉ 2X NO CARTÃO: PREÇO NORMAL;
[ 4 ] EM 3X a NO CARTÃO: 20% DE JUROS; ''')
opcao = int(input('Escolha uma opção: '))
print('A sua compra foi de {},'.format(saldo))
if opcao == 1:
    print('Escolheu a opção [ 1 ], ganhando 10% de desconto, pagando {:.2f} em sua compra!'.format(saldo - (saldo * 0.10)))
elif opcao == 2:
    print('Escolheu a opção [ 2 ], ganhando 5% de desconto, pagando {:.2f} em sua compra!'.format(saldo - (saldo * 0.05)))
elif opcao == 3:
    print('Escolheu a opção [ 3 ], dando 2 parcelas de {:.2f}'.format(saldo / 2))
elif opcao == 4:
    x = int(input('Digite em quantas vezes quer fazer: '))
    print('Escolheu a opção [ 4 ], e fazendo em {} vezes, dando uma parcela de {:.2f}'.format(x, ((saldo * 0.20) + saldo) / x )) 
else: 
    print('Escolha uma opção viavel!!!')