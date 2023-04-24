#Pergunte o salário e apos o salário com um aumento de 15%
salario = float(input('Digite seu salário: '))
aumento = salario*0.15 + salario
print('Seu salário é {:.2f}, porem voce recebeu um aumento de 15% e agora é {:.2f}'.format(salario, aumento))