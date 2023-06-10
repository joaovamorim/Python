
from os import sep


nome = str(input('Digite seu nome completo: ').strip())
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em letras minusculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem ao todo {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O seu nome {} tem {} letras ao todo'.format(separa[0], len(separa[0])))
