#Leia Valor da casa, salário e quantas parcelas vai pagar a casa
#A mensalidade n pode exeder 30% do salário
#mostrar se pode ou não comprar

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario mensal? '))
anos = float(input('Em quantas parcelas voce quer fazer? '))
mensal = valor /  anos
parcela = (mensal * 0.30) + salario
if mensal > parcela:
    print('Desculpe, voce não pode comprar a casa pois excedeu 30% do seu salário, com a parcela de {}'.format(parcela))
elif mensal < parcela:
    print('Sua parcela foi aprovada com a parcela de {}! Parabens'.format(parcela))