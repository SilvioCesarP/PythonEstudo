#Leia Valor da casa, salário e quanto anos vai pagar a casa
#A mensalidade n pode exeder 30% do salário
#mostrar se pode ou não comprar

valor = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salario mensal? '))
anos = float(input('Em quantos anos pretende pagar? '))
mensal = valor /  (anos * 12)
print('O preço escolhido da casa é R${:.2f} e será pago em {:.2f} anos'.format(valor, anos))
print('Sendo a prestação R${:.2f} por mes'.format(mensal))
if mensal > (salario * 0.30) + salario:
    print('Infelizmente voce não podera pagar por essas parcelas!Sendo o seu limite de preço {}'.format((salario * 0.30) + salario))
else:
    print('Parabens voce consegue financiar a casa!')
