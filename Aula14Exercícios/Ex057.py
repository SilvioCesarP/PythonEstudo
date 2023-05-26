#leio sexo de uma pessoa
#Repita até que seja escrito M ou F
#Mostre o resultado

sexo = str(input('Qual o seu sexo [M/F]? ')).strip().upper()[0]
while sexo == 'F'or'M':
    sexo = str(input('Erro, informe seu SEXO [M/F]: '))[0]
print('Cadastro realizado com sucesso')