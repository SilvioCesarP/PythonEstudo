#Leia uma frase
#Mostre ela de tras pra frente e se ela é ou não um polídromo(desconsidere espaço)

frase = str(input('Digite uma frase e te direi se é políndromo ou não: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso = junto[letra]

if junto == inverso:
    print('Temos um políndromo')
else: 
    print('N é um políndromo')