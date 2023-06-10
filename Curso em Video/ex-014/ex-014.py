
print('\033[32m#014 \033[34m- Conversor de Temperaturas')

c = float(input('\033[35mInforme a temperatura em \033[36m°C: '))
f = 9 * c / 5 + 32
print('\033[97mA temperatura em \033[36m{}\033[97m°C para °F é: \033[36m{}\033[97m°F'.format(c, f))
