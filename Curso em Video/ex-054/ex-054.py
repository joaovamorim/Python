
# Coleta a data atual
from datetime import date

ano_atual = date.today().year
total_de_maior = 0
total_de_menor = 0

for pessoas in range(1, 8):
    ano_nascimento = int(input('Em que ano a {}° nasceu: '.format(pessoas)))
    idade = ano_atual - ano_nascimento
    if idade >= 21:
        total_de_maior += 1
    else:
        total_de_menor += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(total_de_maior))
print('Ao todo tivemos {} pessoas menores de idade.'.format(total_de_menor))
