
#   Clássico da Média

nota_1 = float(input('Qual a primeira nota? '))
nota_2 = float(input('Qual a segunda nota? '))
média = (nota_1 + nota_2) / 2

print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}.'.format(nota_1, nota_2, média))

if 7 > média >=5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')
'''else:
    print('O aluno está APROVADO.')'''
