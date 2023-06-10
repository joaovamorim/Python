
# Média Aritimética
titulo = '\033[32m#007 \033[97;7m- Média Aritimética\033[m'
print('\033[33m<>\033[m' * 15)
print(titulo)
print('\033[33m<>\033[m' * 15)

no1 = float(input('\033[35mPrimeira nota do aluno: \033[m'))
no2 = float(input('\033[35mSegunda nota do aluno: \033[m'))
me = (no1 + no2) / 2 # Correto
print('\033[97;1mA média deste aluno é:\033[32m {:.1f}\033[m'.format(me))
# me = no1 + no2 / 2 ( Errado )
# print('A média deste aluno é: {}'.format(me/2))
