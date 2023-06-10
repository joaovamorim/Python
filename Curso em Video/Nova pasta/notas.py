
# Programa que pede uma nota entre 0 e 10 caso o valor seja invalido ele volta um erro e inicia de novo o programa

nota = int(input('Digite uma nota entre 0 e 10: '))

if nota >= 0 and nota <= 10:
    print('Nota recebida, obrigado!')
else:
    print('Nota invalida, tente novamente!')
