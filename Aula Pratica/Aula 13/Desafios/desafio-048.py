
soma = 0

for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma += impar
print('A soma de todos os números multiplos de três é: {}'.format(soma))
