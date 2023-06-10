
print('\033[32m#015 \033[34m- ALUGUEL DE CARROS')

dia = int(input('\033[97mQuantos dias você alugou o carro? '))
km = float(input('Quantos KM você rodou com o carro? '))
re = (60 * dia) + (0.15 * km)
print('O total a pagar é de: \033[34m{}'.format(re))
