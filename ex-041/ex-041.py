
from datetime import date
ano_atual = date.today().year



ano_nascimento = int(input('Ano de nascimento: '))
idade = ano_atual - ano_nascimento

print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificação MIRIM.')
elif idade <= 14:
    print('Classificação INFANTIL.')
elif idade <= 19:
    print('Classificação JUNIOR.')
elif idade <= 25:
    print('Classificação SÊNIOR.')
else:
    print('Classificação MASTER.')
