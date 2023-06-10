
soma = 0

for mumero in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
print('A soma dos números digitados que são pares é: {}'.format(soma))
