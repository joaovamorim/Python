
# Dissecando uma Variável
titulo = '\033[32m#004 \033[33m- Dissecando uma Variável\033[m'
print(titulo)

cores = {'limpa':'\033[m', 'preto':'\033[30;107m', 'vermelho':'\033[31m', 'verde':'\033[32m', 'amarelo':'\033[33m', 'azul':'\033[34m', 'magenta':'\033[35m', 'ciano':'\033[36m', 'branco':'\033[97m'}

algo = input('\033[32mDigite algo: \033[m')
print('{}O tipo primitivo desta frase é: {}'.format(cores['preto'], cores['limpa']),  type(algo))
print('{}Só tem espaços: {}'.format(cores['vermelho'], cores['limpa']), algo.isspace())
print('{}É um numero: {}'.format(cores['verde'], cores['limpa']), algo.isnumeric())
print('{}É alfabetico: {}'.format(cores['amarelo'], cores['limpa']), algo.isalpha())
print('{}É alfanumerico {}'.format(cores['azul'], cores['limpa']), algo.isalnum())
print('{}Esta em letras maiusculas: {}'.format(cores['magenta'], cores['limpa']), algo.isupper())
print('{}Esta em letras minusculas: {}'.format(cores['ciano'], cores['limpa']), algo.islower())
print('{}Esta capitalizada: {}'.format(cores['branco'], cores['limpa']), algo.istitle())
