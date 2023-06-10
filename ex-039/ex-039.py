
from datetime import date


atual = date.today().year
nascimento = int(input('Ano de nascimento? '))
idade = atual - nascimento

print('Quem nasceu em {} tem {} anos em {}.\n'.format(nascimento, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} ano(s) para o ALISTAMENTO MILITAR.'.format(saldo))
    ano = atual + saldo
    print('Seu ALISTAMENTO sera em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você ja deveria ter se ALISTADO há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu ALISTAMENTO foi em {}.'.format(ano))
