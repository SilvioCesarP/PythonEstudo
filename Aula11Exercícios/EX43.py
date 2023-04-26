#leia o peso e a altura
#calcule e mostre o imc
#de acordo com o imc mostre as categorias

peso = float(input('Informe seu peso, em kg: '))
altura = float(input('informe sua altura, em metros: '))
imc = peso / (altura ** 2)

if imc <= 18.5:
    print('Seus IMC é {:.2f}, sendo ABAIXO DO PESO!'.format(imc))
elif imc > 18.5 and imc < 25:
    print('Seu IMC é {:.2f}, sendo no PESO IDEAL!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f}, sendo considerado SOBREPESO (GRAU I)'.format(imc))
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.2f}, sendo considerado OBESIDADE (GRAU II)'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}, sendo considerado OBESIDADE MÓRBIDA (GRAU III)'.format(imc))
else:
    print('Ocorreu algum erro na leitura tente novamente')