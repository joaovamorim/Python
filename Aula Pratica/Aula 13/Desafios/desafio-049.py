
print('Tábuada do 1 a 10')
numero = int(input('Digite um número: '))

print('Você escolheu a tabuada do {}'.format(numero))
for tabuada in range(1, 11):
    print('{} x {} = {}'.format(numero, tabuada, numero*tabuada))
