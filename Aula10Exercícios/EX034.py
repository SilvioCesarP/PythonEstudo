#Leia o salário
#Calcule seu aumento, sendo 1250+ calcule 10% e para inferiores ou iguais 15%

salario = float(input('Digite seu salário: '))
if salario <= 1250:
    aumento = (salario * 0.15) + salario
else:
    aumento = (salario * 0.10) + salario 
print('Seu salário atua é {:.2f}, aumentando para {:.2f}'.format(salario, aumento))
   