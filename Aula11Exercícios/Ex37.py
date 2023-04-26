
#leia um numero inteiro
#Mostre uma escolha para converter para binário, octal, hexadecimal
num = int(input(' Digite um numero: '))
print('''Escolha uma das conversões: 
[ 1 ] converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('{} convertido em BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('ERRO, APENOS NUMEROS DE 1 A 3 SÃO PERMITIDO')

