
#leia duas notas
#Calcule a média
#Mostre se o aluno passou, reproovu ou ficou em recuperação

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7 and media <= 10:
    print('Parabens voce está APROVADO! Com a média em {}'.format(media))
elif media >= 5 and media < 6.9:
    print('Ficou em recuperação! Com a média de {}'.format(media))
elif media < 5 and media >= 0:
    print('Estude mais!!! Voce reprovou, com a média de {}'.format(media))
else:
    print('Erro na leitura das notas! coloque uma nota de 0 a 10!')