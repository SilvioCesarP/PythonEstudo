#crie uma tupla com numeros
#Mostre o numero de acordo com o numero pedido
número = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatrorze', 'quinze', 'sezeseis', 'dezesete', 'dezoito',  'dezenove', 'vinte')

print('='*20)
while True:
    escolha = int(input('Escolha um numero de 0 a 20\nResposta: '))
    if  escolha < 0 or escolha > 20:
        print('tente novamente:')
        
    else:
        print(f'o numero escolhido é {número[escolha]}')
        break
print('='*20)
print('Obrigado por participar!')